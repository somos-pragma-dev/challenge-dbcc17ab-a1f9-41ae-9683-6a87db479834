from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
import uuid


class TransactionType(models.TextChoices):
    INCOME = 'INCOME', 'Ingreso'
    EXPENSE = 'EXPENSE', 'Gasto'
    TRANSFER = 'TRANSFER', 'Transferencia'
    PAYMENT = 'PAYMENT', 'Pago'
    REFUND = 'REFUND', 'Reembolso'
    DEPOSIT = 'DEPOSIT', 'Depósito'
    WITHDRAWAL = 'WITHDRAWAL', 'Retiro'


class TransactionStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pendiente'
    PROCESSING = 'PROCESSING', 'Procesando'
    COMPLETED = 'COMPLETED', 'Completada'
    FAILED = 'FAILED', 'Fallida'
    CANCELLED = 'CANCELLED', 'Cancelada'


class Transaction(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Identificador único de la transacción'
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions',
        help_text='Usuario asociado a la transacción'
    )
    
    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01, message='El monto debe ser mayor que cero'),
            MaxValueValidator(999999999.99, message='El monto excede el límite permitido'),
        ],
        help_text='Monto de la transacción'
    )
    
    currency = models.CharField(
        max_length=3,
        default='COP',
        choices=[('COP', 'Peso Colombiano'), ('USD', 'Dólar'), ('EUR', 'Euro')],
        help_text='Moneda de la transacción'
    )
    
    type = models.CharField(
        max_length=20,
        choices=TransactionType.choices,
        default=TransactionType.EXPENSE,
        help_text='Tipo de transacción'
    )
    
    transaction_type = models.CharField(
        max_length=20,
        choices=TransactionType.choices,
        default=TransactionType.EXPENSE,
        help_text='Tipo de transacción'
    )
    
    status = models.CharField(
        max_length=20,
        choices=TransactionStatus.choices,
        default=TransactionStatus.PENDING,
        help_text='Estado de la transacción'
    )
    
    description = models.TextField(
        blank=True,
        default='',
        help_text='Descripción de la transacción'
    )
    
    category = models.CharField(
        max_length=100,
        blank=True,
        default='',
        help_text='Categoría de la transacción'
    )
    
    reference_number = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        help_text='Número de referencia externo'
    )
    
    reference = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        help_text='Número de referencia externo'
    )
    
    recipient_account = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text='Cuenta del beneficiario'
    )
    
    sender_account = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text='Cuenta del remitente'
    )
    
    metadata = models.JSONField(
        blank=True,
        default=dict,
        help_text='Metadatos adicionales de la transacción'
    )
    
    failure_reason = models.TextField(
        blank=True,
        default='',
        help_text='Razón del fallo de la transacción'
    )
    
    completed_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text='Fecha de completado de la transacción'
    )
    
    date = models.DateField(
        blank=True,
        null=True,
        help_text='Fecha de la transacción'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    processed_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text='Fecha de procesamiento de la transacción'
    )
    
    class Meta:
        db_table = 'transactions'
        verbose_name = 'Transacción'
        verbose_name_plural = 'Transacciones'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'created_at']),
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['transaction_type']),
            models.Index(fields=['reference_number']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return f'{self.transaction_type} - {self.amount} {self.currency} - {self.user.email}'
    
    def clean(self):
        super().clean()
        if self.amount and self.amount <= 0:
            raise ValidationError({'amount': 'El monto debe ser mayor que cero'})
        if self.transaction_type == TransactionType.TRANSFER and not (self.recipient_account or self.sender_account):
            raise ValidationError({'recipient_account': 'Las transferencias requieren cuenta de origen o destino'})
    
    def save(self, *args, **kwargs):
        if not self.reference_number and not self.reference:
            self.reference_number = self.generate_reference()
            self.reference = self.reference_number
        self.full_clean()
        super().save(*args, **kwargs)
    
    def generate_reference(self):
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
        short_uuid = str(self.id)[:8].upper()
        return f'TXN-{timestamp}-{short_uuid}'
    
    def mark_as_completed(self):
        self.status = TransactionStatus.COMPLETED
        self.processed_at = timezone.now()
        self.completed_at = timezone.now()
        self.save(update_fields=['status', 'processed_at', 'completed_at', 'updated_at'])
    
    def mark_as_failed(self, reason=''):
        self.status = TransactionStatus.FAILED
        self.failure_reason = reason
        self.metadata['failure_reason'] = reason
        self.metadata['failed_at'] = timezone.now().isoformat()
        self.save(update_fields=['status', 'failure_reason', 'metadata', 'updated_at'])
    
    def mark_as_cancelled(self):
        self.status = TransactionStatus.CANCELLED
        self.processed_at = timezone.now()
        self.save(update_fields=['status', 'processed_at', 'updated_at'])
    
    def process(self):
        if self.status != TransactionStatus.PENDING:
            raise ValueError(f'No se puede procesar una transacción en estado {self.status}')
        self.status = TransactionStatus.PROCESSING
        self.save(update_fields=['status', 'updated_at'])
        
        try:
            self.mark_as_completed()
        except Exception as e:
            self.mark_as_failed(str(e))
            raise
    
    def is_completed(self):
        return self.status == TransactionStatus.COMPLETED
    
    def is_pending(self):
        return self.status == TransactionStatus.PENDING
    
    def is_failed(self):
        return self.status == TransactionStatus.FAILED
    
    @property
    def is_completed_property(self):
        return self.status == TransactionStatus.COMPLETED
    
    @property
    def is_pending_property(self):
        return self.status == TransactionStatus.PENDING
    
    @property
    def is_failed_property(self):
        return self.status == TransactionStatus.FAILED
    
    @property
    def formatted_amount(self):
        return f'{self.amount:,.2f} {self.currency}'
    
    @property
    def days_since_creation(self):
        return (timezone.now() - self.created_at).days
    
    def get_transaction_type_display(self):
        return self.get_type_display() if self.type else TransactionType(self.transaction_type).label
    
    def get_status_display(self):
        return self.get_status_display()