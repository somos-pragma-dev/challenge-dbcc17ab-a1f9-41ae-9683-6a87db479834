from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='El número de teléfono debe estar en formato: +999999999'
    )
    
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con este correo electrónico',
            'invalid': 'Por favor ingrese un correo electrónico válido',
        }
    )
    
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        help_text='Número de teléfono en formato internacional'
    )
    
    address = models.TextField(
        blank=True,
        default='',
        help_text='Dirección de residencia'
    )
    
    identification_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        help_text='Número de identificación personal'
    )
    
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        help_text='Fecha de nacimiento'
    )
    
    is_verified = models.BooleanField(
        default=False,
        help_text='Indica si el usuario ha verificado su correo electrónico'
    )
    
    last_login_ip = models.GenericIPAddressField(
        blank=True,
        null=True,
        help_text='Dirección IP del último inicio de sesión'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['identification_number']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return full_name if full_name else self.email
    
    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]
    
    def clean(self):
        super().clean()
        if self.email:
            self.email = self.email.lower().strip()
        if self.username:
            self.username = self.username.lower().strip()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def verify_user(self):
        self.is_verified = True
        self.save(update_fields=['is_verified', 'updated_at'])
    
    def update_last_login(self, ip_address):
        self.last_login_ip = ip_address
        self.last_login = timezone.now()
        self.save(update_fields=['last_login_ip', 'last_login', 'updated_at'])
    
    def has_transaction_permission(self):
        return self.is_active and self.is_verified
    
    @property
    def is_complete(self):
        return bool(
            self.first_name and
            self.last_name and
            self.phone and
            self.identification_number and
            self.date_of_birth
        )
    
    @property
    def profile_completion_percentage(self):
        fields = [
            self.first_name,
            self.last_name,
            self.phone,
            self.identification_number,
            self.date_of_birth,
            self.address,
        ]
        completed = sum(1 for f in fields if f)
        return int((completed / len(fields)) * 100)