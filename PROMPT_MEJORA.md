# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Boilerplate del stack que falta

Sin esto no compila ni arranca. Es andamiaje, no toca nada de lo pedagogico:

- **Punto de entrada del stack elegido** — Sin un punto de entrada reconocible, el runtime no tiene por donde arrancar la aplicacion.
- **Capa de interfaz (controller/handler)** — Sin una capa de interfaz explicita, no hay forma de invocar la logica de negocio desde afuera del proceso.

### Archivos que la arquitectura del reto declara y no estan

Creálos con implementacion real, en la capa que les corresponde:

- `api/serializers/__init__.py`
- `api/views/__init__.py`
- `api/tests/__init__.py`

## Como saber que terminaste

```bash
el comando de build o arranque canonico del stack elegido
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Contexto técnico original
API REST con Django Rest Framework y autenticacion

### Reto
- Tema: python-django-rest
- Seniority: junior-l1
- Tipo: theoretical
- Título: Fundamentos de API REST con Django Rest Framework y Autenticación
- Tiempo estimado: 2 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Exploración del Dominio — objetivo: Comprender las necesidades del negocio y los requerimientos funcionales de la API REST. — entregable (NO resolver): Documento que describe los actores, operaciones y criterios de aceptación.
- Fase 2: Diseño de la API — objetivo: Diseñar la estructura de la API REST, incluyendo endpoints y métodos HTTP. — entregable (NO resolver): Diagrama de la estructura de la API, incluyendo endpoints y métodos HTTP.
- Fase 3: Consideraciones de Seguridad — objetivo: Identificar y mitigar riesgos de seguridad en la API REST. — entregable (NO resolver): Documento que describe los riesgos de seguridad identificados y las medidas de mitigación propuestas.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: config/settings.py ===
import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-development-key-change-in-production-environment-12345')

DEBUG = os.environ.get('DEBUG', 'True').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'finance_db'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'api.User'

CORS_ALLOWED_ORIGINS = os.environ.get(
    'CORS_ALLOWED_ORIGINS',
    'http://localhost:3000,http://localhost:8000'
).split(',')

CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

// === ARCHIVO: requirements.txt ===
Django==5.0.6
djangorestframework==3.15.1
djangorestframework-simplejwt==5.3.1
django-cors-headers==4.3.1
psycopg2-binary==2.9.9

// === ARCHIVO: api/models/__init__.py ===
from api.models.user import User
from api.models.transaction import Transaction, TransactionType, TransactionStatus

__all__ = [
    'User',
    'Transaction',
    'TransactionType',
    'TransactionStatus',
]

def get_user_model():
    return User

def get_transaction_model():
    return Transaction

def get_all_models():
    return {
        'User': User,
        'Transaction': Transaction,
    }

def validate_transaction_amount(amount):
    if amount is None:
        raise ValueError('El monto de la transacción no puede ser nulo')
    if not isinstance(amount, (int, float)):
        raise ValueError('El monto debe ser un número')
    if amount <= 0:
        raise ValueError('El monto debe ser mayor que cero')
    return True

def validate_transaction_date(date):
    from django.utils import timezone
    if date is None:
        raise ValueError('La fecha de la transacción no puede ser nula')
    if date > timezone.now():
        raise ValueError('La fecha de la transacción no puede ser futura')
    return True

def get_user_transactions(user):
    from django.db.models import Q
    return Transaction.objects.filter(
        Q(user=user) | Q(user__isnull=False)
    ).select_related('user').order_by('-created_at')

def calculate_user_balance(user):
    from django.db.models import Sum, Q
    income = Transaction.objects.filter(
        user=user,
        type=TransactionType.INCOME,
        status=TransactionStatus.COMPLETED
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    expense = Transaction.objects.filter(
        user=user,
        type=TransactionType.EXPENSE,
        status=TransactionStatus.COMPLETED
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    return income - expense

def get_transactions_by_date_range(user, start_date, end_date):
    from django.db.models import Q
    return Transaction.objects.filter(
        user=user,
        created_at__gte=start_date,
        created_at__lte=end_date
    ).order_by('-created_at')

def get_transactions_by_type(user, transaction_type):
    return Transaction.objects.filter(
        user=user,
        type=transaction_type
    ).order_by('-created_at')

def get_pending_transactions(user):
    return Transaction.objects.filter(
        user=user,
        status=TransactionStatus.PENDING
    ).order_by('-created_at')

def count_user_transactions(user):
    return Transaction.objects.filter(user=user).count()

def get_recent_transactions(user, limit=10):
    return Transaction.objects.filter(
        user=user
    ).select_related('user').order_by('-created_at')[:limit]

// === ARCHIVO: api/models/user.py ===
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

// === ARCHIVO: api/models/transaction.py ===
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
        helpText='Moneda de la transacción'
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
        if not self.reference_number:
            self.reference_number = self.generate_reference()
        self.full_clean()
        super().save(*args, **kwargs)
    
    def generate_reference(self):
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
        short_uuid = str(self.id)[:8].upper()
        return f'TXN-{timestamp}-{short_uuid}'
    
    def mark_as_completed(self):
        self.status = TransactionStatus.COMPLETED
        self.processed_at = timezone.now()
        self.save(update_fields=['status', 'processed_at', 'updated_at'])
    
    def mark_as_failed(self, reason=''):
        self.status = TransactionStatus.FAILED
        self.metadata['failure_reason'] = reason
        self.metadata['failed_at'] = timezone.now().isoformat()
        self.save(update_fields=['status', 'metadata', 'updated_at'])
    
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
    
    @property
    def is_completed(self):
        return self.status == TransactionStatus.COMPLETED
    
    @property
    def is_pending(self):
        return self.status == TransactionStatus.PENDING
    
    @property
    def is_failed(self):
        return self.status == TransactionStatus.FAILED
    
    @property
    def formatted_amount(self):
        return f'{self.amount:,.2f} {self.currency}'
    
    @property
    def days_since_creation(self):
        return (timezone.now() - self.created_at).days


// === ARCHIVO: config/urls.py ===
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from api.views import auth_views, transaction_views

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Endpoints de autenticación JWT
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Rutas de autenticación de usuarios
    path('api/auth/register/', auth_views.RegisterView.as_view(), name='register'),
    path('api/auth/login/', auth_views.LoginView.as_view(), name='login'),
    path('api/auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/auth/profile/', auth_views.ProfileView.as_view(), name='profile'),
    path('api/auth/change-password/', auth_views.ChangePasswordView.as_view(), name='change_password'),
    
    # Rutas de transacciones
    path('api/transactions/', transaction_views.TransactionListCreateView.as_view(), name='transaction_list_create'),
    path('api/transactions/<int:pk>/', transaction_views.TransactionDetailView.as_view(), name='transaction_detail'),
    path('api/transactions/<int:pk>/complete/', transaction_views.TransactionCompleteView.as_view(), name='transaction_complete'),
    path('api/transactions/<int:pk>/cancel/', transaction_views.TransactionCancelView.as_view(), name='transaction_cancel'),
    path('api/transactions/<int:pk>/fail/', transaction_views.TransactionFailView.as_view(), name='transaction_fail'),
    
    # Rutas de consulta de transacciones
    path('api/transactions/user/<int:user_id>/', transaction_views.UserTransactionsView.as_view(), name='user_transactions'),
    path('api/transactions/balance/<int:user_id>/', transaction_views.UserBalanceView.as_view(), name='user_balance'),
    path('api/transactions/by-date-range/', transaction_views.TransactionsByDateRangeView.as_view(), name='transactions_by_date_range'),
    path('api/transactions/by-type/', transaction_views.TransactionsByTypeView.as_view(), name='transactions_by_type'),
    path('api/transactions/pending/', transaction_views.PendingTransactionsView.as_view(), name='pending_transactions'),
    path('api/transactions/recent/', transaction_views.RecentTransactionsView.as_view(), name='recent_transactions'),
    path('api/transactions/stats/', transaction_views.TransactionStatsView.as_view(), name='transaction_stats'),
    
    # Endpoint de verificación de salud de la API
    path('api/health/', auth_views.HealthCheckView.as_view(), name='health_check'),
]

// === ARCHIVO: api/serializers/__init__.py ===
// === ARCHIVO: api/serializers/user_serializer.py ===
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=False)
    full_name = serializers.SerializerMethodField()
    short_name = serializers.SerializerMethodField()
    profile_completion = serializers.SerializerMethodField()
    transaction_permission = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'full_name', 'short_name', 'profile_completion', 'transaction_permission',
            'is_active', 'is_verified', 'date_joined', 'last_login',
            'password', 'password_confirm'
        ]
        read_only_fields = ['id', 'date_joined', 'last_login', 'is_verified']
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    
    def get_short_name(self, obj):
        return obj.get_short_name()
    
    def get_profile_completion(self, obj):
        return obj.profile_completion_percentage()
    
    def get_transaction_permission(self, obj):
        return obj.has_transaction_permission()
    
    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        
        if self.instance is None and not password:
            raise serializers.ValidationError({'password': 'La contraseña es obligatoria para nuevos usuarios'})
        
        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError({'password_confirm': 'Las contraseñas no coinciden'})
        
        if password and len(password) < 8:
            raise serializers.ValidationError({'password': 'La contraseña debe tener al menos 8 caracteres'})
        
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm', None)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        validated_data.pop('password_confirm', None)
        password = validated_data.pop('password', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not self.context.get('include_sensitive', False):
            data.pop('password', None)
            data.pop('password_confirm', None)
        return data


class UserRegistrationSerializer(UserSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['username'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class UserProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    short_name = serializers.SerializerMethodField()
    profile_completion = serializers.SerializerMethodField()
    transaction_permission = serializers.SerializerMethodField()
    recent_transactions = serializers.SerializerMethodField()
    total_transactions = serializers.SerializerMethodField()
    account_balance = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'full_name', 'short_name', 'profile_completion', 'transaction_permission',
            'is_active', 'is_verified', 'date_joined', 'last_login',
            'recent_transactions', 'total_transactions', 'account_balance'
        ]
        read_only_fields = fields
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    
    def get_short_name(self, obj):
        return obj.get_short_name()
    
    def get_profile_completion(self, obj):
        return obj.profile_completion_percentage()
    
    def get_transaction_permission(self, obj):
        return obj.has_transaction_permission()
    
    def get_recent_transactions(self, obj):
        from api.models import get_recent_transactions
        transactions = get_recent_transactions(obj, limit=5)
        from api.serializers.transaction_serializer import TransactionSummarySerializer
        return TransactionSummarySerializer(transactions, many=True).data
    
    def get_total_transactions(self, obj):
        from api.models import count_user_transactions
        return count_user_transactions(obj)
    
    def get_account_balance(self, obj):
        from api.models import calculate_user_balance
        return calculate_user_balance(obj)


class UserListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    profile_completion = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'is_active', 'is_verified', 'profile_completion']
        read_only_fields = fields
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    
    def get_profile_completion(self, obj):
        return obj.profile_completion_percentage()
// === ARCHIVO: api/serializers/transaction_serializer.py ===
from rest_framework import serializers
from django.utils import timezone
from api.models.transaction import Transaction, TransactionType, TransactionStatus
from api.models import validate_transaction_amount, validate_transaction_date, get_user_transactions


class TransactionSerializer(serializers.ModelSerializer):
    transaction_type_display = serializers.CharField(source='get_transaction_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    formatted_amount = serializers.SerializerMethodField()
    days_since_creation = serializers.SerializerMethodField()
    can_cancel = serializers.SerializerMethodField()
    can_retry = serializers.SerializerMethodField()
    user_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Transaction
        fields = [
            'id', 'user', 'user_info', 'transaction_type', 'transaction_type_display',
            'amount', 'formatted_amount', 'status', 'status_display', 'reference',
            'description', 'created_at', 'updated_at', 'completed_at', 'failure_reason',
            'days_since_creation', 'can_cancel', 'can_retry'
        ]
        read_only_fields = [
            'id', 'reference', 'created_at', 'updated_at', 'completed_at', 'failure_reason'
        ]
    
    def get_formatted_amount(self, obj):
        return obj.formatted_amount()
    
    def get_days_since_creation(self, obj):
        return obj.days_since_creation()
    
    def get_can_cancel(self, obj):
        return obj.is_pending()
    
    def get_can_retry(self, obj):
        return obj.is_failed()
    
    def get_user_info(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'email': obj.user.email
        }
    
    def validate_amount(self, value):
        if not validate_transaction_amount(value):
            raise serializers.ValidationError('El monto debe ser mayor que cero')
        return value
    
    def validate_transaction_type(self, value):
        valid_types = [choice[0] for choice in TransactionType.choices]
        if value not in valid_types:
            raise serializers.ValidationError(f'Tipo de transacción inválido. Opciones válidas: {valid_types}')
        return value
    
    def validate_status(self, value):
        valid_statuses = [choice[0] for choice in TransactionStatus.choices]
        if value not in valid_statuses:
            raise serializers.ValidationError(f'Estado inválido. Opciones válidas: {valid_statuses}')
        return value
    
    def create(self, validated_data):
        validated_data['reference'] = Transaction().generate_reference()
        return super().create(validated_data)


class TransactionSummarySerializer(serializers.ModelSerializer):
    transaction_type_display = serializers.CharField(source='get_transaction_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    formatted_amount = serializers.SerializerMethodField()
    
    class Meta:
        model = Transaction
        fields = [
            'id', 'transaction_type', 'transaction_type_display',
            'amount', 'formatted_amount', 'status', 'status_display',
            'reference', 'created_at'
        ]
        read_only_fields = fields
    
    def get_formatted_amount(self, obj):
        return obj.formatted_amount()


class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount', 'description']
    
    def validate_amount(self, value):
        if not validate_transaction_amount(value):
            raise serializers.ValidationError('El monto debe ser mayor que cero')
        if value > 1000000:
            raise serializers.ValidationError('El monto excede el límite permitido de 1,000,000')
        return value
    
    def validate_transaction_type(self, value):
        valid_types = [choice[0] for choice in TransactionType.choices]
        if value not in valid_types:
            raise serializers.ValidationError(f'Tipo de transacción inválido')
        return value
    
    def create(self, validated_data):
        user = self.context['request'].user
        transaction = Transaction.objects.create(
            user=user,
            transaction_type=validated_data['transaction_type'],
            amount=validated_data['amount'],
            description=validated_data.get('description', ''),
            status=TransactionStatus.PENDING
        )
        return transaction


class TransactionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['status', 'failure_reason']
    
    def validate_status(self, value):
        valid_statuses = [choice[0] for choice in TransactionStatus.choices]
        if value not in valid_statuses:
            raise serializers.ValidationError(f'Estado inválido')
        return value
    
    def validate(self, attrs):
        instance = self.instance
        if instance.status == TransactionStatus.COMPLETED:
            raise serializers.ValidationError('No se puede modificar una transacción completada')
        if instance.status == TransactionStatus.CANCELLED:
            raise serializers.ValidationError('No se puede modificar una transacción cancelada')
        if attrs.get('status') == TransactionStatus.FAILED and not attrs.get('failure_reason'):
            raise serializers.ValidationError('Debe proporcionar una razón de fallo')
        return attrs


class TransactionFilterSerializer(serializers.Serializer):
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    transaction_type = serializers.ChoiceField(choices=TransactionType.choices, required=False)
    status = serializers.ChoiceField(choices=TransactionStatus.choices, required=False)
    min_amount = serializers.DecimalField(max_digits=12, decimal_places=2, required=False)
    max_amount = serializers.DecimalField(max_digits=12, decimal_places=2, required=False)
    
    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError('La fecha inicial no puede ser mayor que la final')
        min_amount = attrs.get('min_amount')
        max_amount = attrs.get('max_amount')
        if min_amount and max_amount and min_amount > max_amount:
            raise serializers.ValidationError('El monto mínimo no puede ser mayor que el máximo')
        return attrs
    
    def validate_start_date(self, value):
        if value and not validate_transaction_date(value):
            raise serializers.ValidationError('Fecha inválida')
        return value
    
    def validate_end_date(self, value):
        if value and not validate_transaction_date(value):
            raise serializers.ValidationError('Fecha inválida')
        return value


class TransactionStatusUpdateSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=['complete', 'fail', 'cancel'])
    failure_reason = serializers.CharField(required=False, allow_blank=True)
    
    def validate_action(self, value):
        return value
    
    def validate(self, attrs):
        action = attrs.get('action')
        failure_reason = attrs.get('failure_reason')
        if action == 'fail' and not failure_reason:
            raise serializers.ValidationError({'failure_reason': 'Razón de fallo requerida'})
        return attrs


// === ARCHIVO: api/views/__init__.py ===
// === ARCHIVO: api/views/auth_views.py ===
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    Autentica un usuario y retorna tokens JWT.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'Usuario y contraseña son requeridos'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response(
            {'error': 'Credenciales inválidas'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    if not user.is_active:
        return Response(
            {'error': 'Usuario inactivo'},
            status=status.HTTP_403_FORBIDDEN
        )
    
    user.update_last_login(ip_address=_get_client_ip(request))
    
    refresh = RefreshToken.for_user(user)
    
    return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'full_name': user.get_full_name(),
        }
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    Cierra la sesión del usuario invalidando el token.
    """
    try:
        refresh_token = request.data.get('refresh')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        return Response(
            {'message': 'Sesión cerrada exitosamente'},
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {'error': 'Token inválido o ya expirado'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    Registra un nuevo usuario en el sistema.
    """
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name', '')
    last_name = request.data.get('last_name', '')
    
    if not username or not email or not password:
        return Response(
            {'error': 'Usuario, email y contraseña son requeridos'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'El nombre de usuario ya está en uso'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(email=email).exists():
        return Response(
            {'error': 'El correo electrónico ya está registrado'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = User.objects.create(
        username=username,
        email=email,
        password=make_password(password),
        first_name=first_name,
        last_name=last_name,
    )
    
    user.verify_user()
    
    refresh = RefreshToken.for_user(user)
    
    return Response({
        'message': 'Usuario registrado exitosamente',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        },
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
    """
    Retorna la información del usuario actualmente autenticado.
    """
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'full_name': user.get_full_name(),
        'short_name': user.get_short_name(),
        'is_complete': user.is_complete(),
        'completion_percentage': user.profile_completion_percentage(),
        'has_transaction_permission': user.has_transaction_permission(),
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def refresh_token_view(request):
    """
    Refresca el token de acceso usando el token de refresh.
    """
    try:
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response(
                {'error': 'Token de refresh es requerido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        token = RefreshToken(refresh_token)
        return Response({
            'access': str(token.access_token),
            'refresh': str(token),
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {'error': 'Token de refresh inválido'},
            status=status.HTTP_401_UNAUTHORIZED
        )


def _get_client_ip(request):
    """
    Extrae la dirección IP del cliente de la petición.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
// === ARCHIVO: api/views/transaction_views.py ===
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime

from api.models import (
    get_user_model,
    get_transaction_model,
    validate_transaction_amount,
    validate_transaction_date,
    get_user_transactions,
    calculate_user_balance,
    get_transactions_by_date_range,
    get_transactions_by_type,
    get_pending_transactions,
    count_user_transactions,
    get_recent_transactions,
)

User = get_user_model()
Transaction = get_transaction_model()


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def transaction_list_create_view(request):
    """
    Lista todas las transacciones del usuario autenticado o crea una nueva.
    """
    if request.method == 'GET':
        user = request.user
        transactions = get_user_transactions(user)
        
        transaction_type = request.query_params.get('type')
        if transaction_type:
            transactions = get_transactions_by_type(user, transaction_type)
        
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if start_date and end_date:
            try:
                start = datetime.fromisoformat(start_date)
                end = datetime.fromisoformat(end_date)
                transactions = get_transactions_by_date_range(user, start, end)
            except ValueError:
                return Response(
                    {'error': 'Formato de fecha inválido. Use ISO 8601.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        pending_only = request.query_params.get('pending')
        if pending_only and pending_only.lower() == 'true':
            transactions = get_pending_transactions(user)
        
        limit = request.query_params.get('limit', '10')
        try:
            limit = int(limit)
            if limit > 0:
                transactions = get_recent_transactions(user, limit=limit)
        except ValueError:
            pass
        
        total_count = count_user_transactions(user)
        balance = calculate_user_balance(user)
        
        transaction_data = []
        for t in transactions:
            transaction_data.append({
                'id': t.id,
                'reference': t.generate_reference(),
                'type': t.type,
                'status': t.status,
                'amount': t.formatted_amount(),
                'amount_raw': str(t.amount),
                'description': t.description,
                'date': t.date.isoformat() if t.date else None,
                'created_at': t.created_at.isoformat() if hasattr(t, 'created_at') else None,
                'is_completed': t.is_completed(),
                'is_pending': t.is_pending(),
                'is_failed': t.is_failed(),
                'days_since_creation': t.days_since_creation() if hasattr(t, 'days_since_creation') else None,
            })
        
        return Response({
            'transactions': transaction_data,
            'total_count': total_count,
            'balance': str(balance),
            'user': {
                'id': user.id,
                'username': user.username,
                'full_name': user.get_full_name(),
            }
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        return _create_transaction(request)


def _create_transaction(request):
    """
    Crea una nueva transacción para el usuario autenticado.
    """
    user = request.user
    
    if not user.has_transaction_permission():
        return Response(
            {'error': 'Usuario no tiene permisos para crear transacciones'},
            status=status.HTTP_403_FORBIDDEN
        )
    
    amount = request.data.get('amount')
    transaction_type = request.data.get('type')
    description = request.data.get('description', '')
    date = request.data.get('date')
    
    if not amount or not transaction_type:
        return Response(
            {'error': 'Monto y tipo de transacción son requeridos'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        amount = validate_transaction_amount(amount)
    except ValueError as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    transaction_date = None
    if date:
        try:
            transaction_date = validate_transaction_date(date)
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    transaction = Transaction.objects.create(
        user=user,
        amount=amount,
        type=transaction_type,
        description=description,
        date=transaction_date or timezone.now().date(),
        status=Transaction.TransactionStatus.PENDING,
    )
    
    transaction.generate_reference()
    transaction.save()
    
    return Response({
        'message': 'Transacción creada exitosamente',
        'transaction': {
            'id': transaction.id,
            'reference': transaction.generate_reference(),
            'type': transaction.type,
            'status': transaction.status,
            'amount': transaction.formatted_amount(),
            'amount_raw': str(transaction.amount),
            'description': transaction.description,
            'date': transaction.date.isoformat() if transaction.date else None,
            'created_at': transaction.created_at.isoformat() if hasattr(transaction, 'created_at') else None,
        }
    }, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def transaction_detail_view(request, pk):
    """
    Obtiene, actualiza o elimina una transacción específica.
    """
    user = request.user
    transaction = get_object_or_404(Transaction, pk=pk, user=user)
    
    if request.method == 'GET':
        return _get_transaction_detail(transaction)
    elif request.method in ['PUT', 'PATCH']:
        return _update_transaction(request, transaction)
    elif request.method == 'DELETE':
        return _delete_transaction(transaction)


def _get_transaction_detail(transaction):
    """
    Retorna el detalle de una transacción.
    """
    return Response({
        'id': transaction.id,
        'reference': transaction.generate_reference(),
        'type': transaction.type,
        'status': transaction.status,
        'amount': transaction.formatted_amount(),
        'amount_raw': str(transaction.amount),
        'description': transaction.description,
        'date': transaction.date.isoformat() if transaction.date else None,
        'created_at': transaction.created_at.isoformat() if hasattr(transaction, 'created_at') else None,
        'updated_at': transaction.updated_at.isoformat() if hasattr(transaction, 'updated_at') else None,
        'is_completed': transaction.is_completed(),
        'is_pending': transaction.is_pending(),
        'is_failed': transaction.is_failed(),
        'days_since_creation': transaction.days_since_creation() if hasattr(transaction, 'days_since_creation') else None,
    }, status=status.HTTP_200_OK)


def _update_transaction(request, transaction):
    """
    Actualiza una transacción existente.
    """
    if transaction.is_completed():
        return Response(
            {'error': 'No se puede modificar una transacción completada'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    amount = request.data.get('amount')
    description = request.data.get('description')
    new_status = request.data.get('status')
    
    if amount:
        try:
            validated_amount = validate_transaction_amount(amount)
            transaction.amount = validated_amount
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    if description is not None:
        transaction.description = description
    
    if new_status:
        if new_status == 'completed':
            transaction.mark_as_completed()
        elif new_status == 'failed':
            reason = request.data.get('reason', '')
            transaction.mark_as_failed(reason)
        elif new_status == 'cancelled':
            transaction.mark_as_cancelled()
        else:
            return Response(
                {'error': 'Estado inválido. Use: completed, failed, cancelled'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    transaction.save()
    
    return Response({
        'message': 'Transacción actualizada exitosamente',
        'transaction': {
            'id': transaction.id,
            'reference': transaction.generate_reference(),
            'type': transaction.type,
            'status': transaction.status,
            'amount': transaction.formatted_amount(),
            'amount_raw': str(transaction.amount),
            'description': transaction.description,
            'date': transaction.date.isoformat() if transaction.date else None,
        }
    }, status=status.HTTP_200_OK)


def _delete_transaction(transaction):
    """
    Elimina una transacción.
    """
    if transaction.is_completed():
        return Response(
            {'error': 'No se puede eliminar una transacción completada'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    transaction_id = transaction.id
    transaction.delete()
    
    return Response({
        'message': f'Transacción {transaction_id} eliminada exitosamente'
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transaction_process_view(request, pk):
    """
    Procesa una transacción pendiente.
    """
    user = request.user
    transaction = get_object_or_404(Transaction, pk=pk, user=user)
    
    if not transaction.is_pending():
        return Response(
            {'error': 'Solo se pueden procesar transacciones pendientes'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        transaction.process()
        transaction.save()
        
        return Response({
            'message': 'Transacción procesada exitosamente',
            'transaction': {
                'id': transaction.id,
                'reference': transaction.generate_reference(),
                'status': transaction.status,
                'is_completed': transaction.is_completed(),
            }
        }, status=status.HTTP_200_OK)
    except Exception as e:
        transaction.mark_as_failed(str(e))
        transaction.save()
        return Response(
            {'error': f'Error al procesar transacción: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transaction_balance_view(request):
    """
    Retorna el balance actual del usuario.
    """
    user = request.user
    balance = calculate_user_balance(user)
    
    return Response({
        'balance': str(balance),
        'user_id': user.id,
        'username': user.username,
    }, status=status.HTTP_200_OK)


=== ARCHIVO: api/tests/__init__.py ===

=== ARCHIVO: api/tests/test_auth.py ===
import pytest
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from api.models.user import User
from api.models.transaction import Transaction, TransactionType, TransactionStatus


class AuthViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.logout_url = reverse('logout')
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'SecurePassword123!',
            'password_confirm': 'SecurePassword123!',
            'first_name': 'Test',
            'last_name': 'User'
        }
        self.user = User.objects.create_user(
            username='existinguser',
            email='existing@example.com',
            password='ExistingPassword123!'
        )

    def test_user_registration_success(self):
        response = self.client.post(
            self.register_url,
            data=self.user_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user', response.data)
        self.assertIn('tokens', response.data)
        self.assertEqual(response.data['user']['email'], self.user_data['email'])
        self.assertTrue(User.objects.filter(email=self.user_data['email']).exists())

    def test_user_registration_password_mismatch(self):
        invalid_data = self.user_data.copy()
        invalid_data['password_confirm'] = 'DifferentPassword123!'
        response = self.client.post(
            self.register_url,
            data=invalid_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_user_registration_duplicate_email(self):
        duplicate_data = self.user_data.copy()
        duplicate_data['email'] = self.user.email
        response = self.client.post(
            self.register_url,
            data=duplicate_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_user_registration_duplicate_username(self):
        duplicate_data = self.user_data.copy()
        duplicate_data['username'] = self.user.username
        response = self.client.post(
            self.register_url,
            data=duplicate_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_user_login_success(self):
        login_data = {
            'username': self.user.username,
            'password': 'ExistingPassword123!'
        }
        response = self.client.post(
            self.login_url,
            data=login_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_login_invalid_credentials(self):
        invalid_login = {
            'username': self.user.username,
            'password': 'WrongPassword123!'
        }
        response = self.client.post(
            self.login_url,
            data=invalid_login,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_login_nonexistent_user(self):
        login_data = {
            'username': 'nonexistentuser',
            'password': 'SomePassword123!'
        }
        response = self.client.post(
            self.login_url,
            data=login_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_refresh(self):
        refresh = RefreshToken.for_user(self.user)
        refresh_url = reverse('token_refresh')
        refresh_data = {'refresh': str(refresh)}
        response = self.client.post(
            refresh_url,
            data=refresh_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_protected_endpoint_without_token(self):
        protected_url = reverse('transaction-list')
        response = self.client.get(protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_protected_endpoint_with_valid_token(self):
        refresh = RefreshToken.for_user(self.user)
        protected_url = reverse('transaction-list')
        response = self.client.get(
            protected_url,
            HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_protected_endpoint_with_invalid_token(self):
        protected_url = reverse('transaction-list')
        response = self.client.get(
            protected_url,
            HTTP_AUTHORIZATION='Bearer invalidtoken123'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='modeltestuser',
            email='modeltest@example.com',
            password='TestPassword123!'
        )

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'modeltestuser')

    def test_user_get_full_name(self):
        self.user.first_name = 'John'
        self.user.last_name = 'Doe'
        self.assertEqual(self.user.get_full_name(), 'John Doe')

    def test_user_get_short_name(self):
        self.user.first_name = 'John'
        self.assertEqual(self.user.get_short_name(), 'John')

    def test_user_verification(self):
        self.assertFalse(self.user.is_verified)
        self.user.verify_user()
        self.assertTrue(self.user.is_verified)

    def test_user_profile_completion_incomplete(self):
        percentage = self.user.profile_completion_percentage()
        self.assertLess(percentage, 100)

    def test_user_profile_completion_complete(self):
        self.user.first_name = 'Complete'
        self.user.last_name = 'User'
        self.user.phone = '+1234567890'
        self.user.address = '123 Main St'
        self.user.save()
        percentage = self.user.profile_completion_percentage()
        self.assertEqual(percentage, 100)


class AuthenticationSecurityTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('token_obtain_pair')
        self.user = User.objects.create_user(
            username='securityuser',
            email='security@example.com',
            password='SecurePass123!'
        )

    def test_sql_injection_in_login(self):
        malicious_data = {
            'username': "admin' OR '1'='1",
            'password': 'anypassword'
        }
        response = self.client.post(
            self.login_url,
            data=malicious_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_brute_force_protection(self):
        login_data = {
            'username': self.user.username,
            'password': 'WrongPassword!'
        }
        for i in range(5):
            response = self.client.post(
                self.login_url,
                data=login_data,
                content_type='application/json'
            )
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_xss_in_registration(self):
        malicious_data = {
            'username': '<script>alert(1)</script>',
            'email': 'xss@example.com',
            'password': 'Password123!',
            'password_confirm': 'Password123!'
        }
        response = self.client.post(
            reverse('register'),
            data=malicious_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


=== ARCHIVO: api/tests/test_transactions.py ===
import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from api.models.user import User
from api.models.transaction import Transaction, TransactionType, TransactionStatus


class TransactionViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='transactionuser',
            email='transaction@example.com',
            password='UserPassword123!'
        )
        self.refresh = RefreshToken.for_user(self.user)
        self.transaction_list_url = reverse('transaction-list')
        self.transaction_detail_url = lambda pk: reverse('transaction-detail', kwargs={'pk': pk})
        Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.DEPOSIT,
            amount=1000.00,
            status=TransactionStatus.COMPLETED,
            description='Test deposit'
        )
        Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.WITHDRAWAL,
            amount=250.50,
            status=TransactionStatus.PENDING,
            description='Test withdrawal'
        )
        Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.TRANSFER,
            amount=500.00,
            status=TransactionStatus.FAILED,
            description='Failed transfer'
        )

    def test_list_transactions_authenticated(self):
        response = self.client.get(
            self.transaction_list_url,
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_transactions_unauthenticated(self):
        response = self.client.get(self.transaction_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_transaction_deposit(self):
        transaction_data = {
            'transaction_type': TransactionType.DEPOSIT,
            'amount': 1500.00,
            'description': 'New deposit transaction'
        }
        response = self.client.post(
            self.transaction_list_url,
            data=transaction_data,
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(float(response.data['amount']), 1500.00)
        self.assertEqual(response.data['transaction_type'], TransactionType.DEPOSIT)

    def test_create_transaction_invalid_amount(self):
        invalid_data = {
            'transaction_type': TransactionType.DEPOSIT,
            'amount': -100.00,
            'description': 'Invalid amount'
        }
        response = self.client.post(
            self.transaction_list_url,
            data=invalid_data,
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('amount', response.data)

    def test_create_transaction_zero_amount(self):
        zero_data = {
            'transaction_type': TransactionType.TRANSFER,
            'amount': 0.00,
            'description': 'Zero amount'
        }
        response = self.client.post(
            self.transaction_list_url,
            data=zero_data,
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_transaction_detail(self):
        transaction = Transaction.objects.filter(user=self.user).first()
        url = self.transaction_detail_url(transaction.pk)
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], transaction.pk)

    def test_retrieve_other_user_transaction_forbidden(self):
        other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='OtherPassword123!'
        )
        other_transaction = Transaction.objects.create(
            user=other_user,
            transaction_type=TransactionType.DEPOSIT,
            amount=999.00,
            status=TransactionStatus.COMPLETED
        )
        url = self.transaction_detail_url(other_transaction.pk)
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_transaction_status(self):
        transaction = Transaction.objects.filter(
            user=self.user,
            status=TransactionStatus.PENDING
        ).first()
        url = self.transaction_detail_url(transaction.pk)
        update_data = {'status': TransactionStatus.COMPLETED}
        response = self.client.patch(
            url,
            data=update_data,
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        transaction.refresh_from_db()
        self.assertEqual(transaction.status, TransactionStatus.COMPLETED)

    def test_delete_transaction(self):
        transaction = Transaction.objects.filter(user=self.user).first()
        url = self.transaction_detail_url(transaction.pk)
        response = self.client.delete(
            url,
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Transaction.objects.filter(pk=transaction.pk).exists())


class TransactionFilterTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='filteruser',
            email='filter@example.com',
            password='FilterPassword123!'
        )
        self.refresh = RefreshToken.for_user(self.user)
        self.list_url = reverse('transaction-list')
        now = timezone.now()
        Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.DEPOSIT,
            amount=100.00,
            status=TransactionStatus.COMPLETED,
            created_at=now - timedelta(days=10)
        )
        Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.WITHDRAWAL,
            amount=200.00,
            status=TransactionStatus.PENDING,
            created_at=now - timedelta(days=5)
        )
        Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.TRANSFER,
            amount=300.00,
            status=TransactionStatus.COMPLETED,
            created_at=now
        )

    def test_filter_by_type(self):
        response = self.client.get(
            f'{self.list_url}?type={TransactionType.DEPOSIT}',
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertEqual(item['transaction_type'], TransactionType.DEPOSIT)

    def test_filter_by_status(self):
        response = self.client.get(
            f'{self.list_url}?status={TransactionStatus.PENDING}',
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertEqual(item['status'], TransactionStatus.PENDING)

    def test_filter_by_date_range(self):
        start_date = (timezone.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        end_date = timezone.now().strftime('%Y-%m-%d')
        response = self.client.get(
            f'{self.list_url}?start_date={start_date}&end_date={end_date}',
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_by_min_amount(self):
        response = self.client.get(
            f'{self.list_url}?min_amount=150',
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertGreaterEqual(float(item['amount']), 150)

    def test_filter_by_max_amount(self):
        response = self.client.get(
            f'{self.list_url}?max_amount=250',
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertLessEqual(float(item['amount']), 250)


class TransactionModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='modeltest',
            email='modeltest@example.com',
            password='ModelTest123!'
        )

    def test_transaction_str_representation(self):
        transaction = Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.DEPOSIT,
            amount=500.00,
            status=TransactionStatus.COMPLETED
        )
        expected = f'{transaction.transaction_type} - {transaction.amount}'
        self.assertEqual(str(transaction), expected)

    def test_transaction_generate_reference(self):
        transaction = Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.WITHDRAWAL,
            amount=100.00,
            status=TransactionStatus.PENDING
        )
        self.assertIsNotNone(transaction.reference)
        self.assertTrue(transaction.reference.startswith('TXN-'))

    def test_transaction_mark_as_completed(self):
        transaction = Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.TRANSFER,
            amount=200.00,
            status=TransactionStatus.PENDING
        )
        transaction.mark_as_completed()
        self.assertEqual(transaction.status, TransactionStatus.COMPLETED)

    def test_transaction_mark_as_failed(self):
        transaction = Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.DEPOSIT,
            amount=300.00,
            status=TransactionStatus.PENDING
        )
        transaction.mark_as_failed('Insufficient funds')
        self.assertEqual(transaction.status, TransactionStatus.FAILED)
        self.assertEqual(transaction.failure_reason, 'Insufficient funds')

    def test_transaction_mark_as_cancelled(self):
        transaction = Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.WITHDRAWAL,
            amount=150.00,
            status=TransactionStatus.PENDING
        )
        transaction.mark_as_cancelled()
        self.assertEqual(transaction.status, TransactionStatus.CANCELLED)

    def test_transaction_is_completed(self):
        transaction = Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.DEPOSIT,
            amount=100.00,
            status=TransactionStatus.COMPLETED
        )
        self.assertTrue(transaction.is_completed())
        self.assertFalse(transaction.is_pending())
        self.assertFalse(transaction.is_failed())

    def test_transaction_formatted_amount(self):
        transaction = Transaction.objects.create(
            user=self.user,
            transaction_type=TransactionType.DEPOSIT,
            amount=1234.56,
            status=TransactionStatus.COMPLETED
        )
        formatted = transaction.formatted_amount()
        self.assertIn('1,234.56', formatted)


class TransactionSecurityTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='secureuser',
            email='secure@example.com',
            password='SecurePass123!'
        )
        self.refresh = RefreshToken.for_user(self.user)
        self.other_user = User.objects.create_user(
            username='othersecure',
            email='othersecure@example.com',
            password='OtherSecure123!'
        )
        self.transaction = Transaction.objects.create(
            user=self.other_user,
            transaction_type=TransactionType.DEPOSIT,
            amount=5000.00,
            status=TransactionStatus.COMPLETED
        )

    def test_user_cannot_access_other_user_transactions(self):
        url = reverse('transaction-detail', kwargs={'pk': self.transaction.pk})
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cannot_modify_other_user_transaction(self):
        url = reverse('transaction-detail', kwargs={'pk': self.transaction.pk})
        response = self.client.patch(
            url,
            data={'status': TransactionStatus.CANCELLED},
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.transaction.refresh_from_db()
        self.assertEqual(self.transaction.status, TransactionStatus.COMPLETED)

    def test_user_cannot_delete_other_user_transaction(self):
        url = reverse('transaction-detail', kwargs={'pk': self.transaction.pk})
        response = self.client.delete(
            url,
            HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(Transaction.objects.filter(pk=self.transaction.pk).exists())


// === ARCHIVO: manage.py ===
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    execute_from_command_line(sys.argv)


def check_environment():
    """Verify that the environment is properly configured."""
    required_vars = ['DJANGO_SETTINGS_MODULE']
    missing = [var for var in required_vars if not os.environ.get(var)]
    
    if missing:
        print(f"Warning: Missing environment variables: {', '.join(missing)}")
        return False
    return True


def run_migrations():
    """Execute database migrations."""
    print("Running migrations...")
    execute_from_command_line(['manage.py', 'migrate', '--verbosity=2'])


def create_superuser():
    """Create an admin superuser interactively."""
    print("Creating superuser...")
    execute_from_command_line(['manage.py', 'createsuperuser'])


def run_tests():
    """Run the test suite."""
    print("Running tests...")
    execute_from_command_line(['manage.py', 'test', '--verbosity=2'])


def collect_static_files():
    """Collect static files to the configured directory."""
    print("Collecting static files...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])


def check_system():
    """Perform system checks to identify configuration issues."""
    print("Performing system checks...")
    execute_from_command_line(['manage.py', 'check'])


def show_urls():
    """Display all URL routes in the application."""
    print("Available URL patterns:")
    execute_from_command_line(['manage.py', 'show_urls'])


def make_migrations(app_name=None):
    """Create new migrations based on model changes."""
    if app_name:
        print(f"Creating migrations for {app_name}...")
        execute_from_command_line(['manage.py', 'makemigrations', app_name])
    else:
        print("Creating migrations for all apps...")
        execute_from_command_line(['manage.py', 'makemigrations'])


def shell_plus():
    """Open Django shell with extended features."""
    try:
        from django_extensions.management import shell_plus
        shell_plus()
    except ImportError:
        print("django-extensions not installed. Using default shell.")
        execute_from_command_line(['manage.py', 'shell'])


def get_project_root():
    """Return the absolute path to the project root directory."""
    return Path(__file__).resolve().parent


def setup_django_environ():
    """Configure Django environment settings."""
    root = get_project_root()
    
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    os.environ.setdefault('DJANGO_SECRET_KEY', os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-key-change-in-production'))
    os.environ.setdefault('DEBUG', os.environ.get('DEBUG', 'True'))


def run_server(host='127.0.0.1', port=8000, reload=True):
    """Start the development server."""
    cmd = ['manage.py', 'runserver', f'{host}:{port}']
    if reload:
        cmd.append('--noreload')
    
    subprocess.run(cmd)


def database_command(command):
    """Execute a database management command."""
    valid_commands = ['migrate', 'makemigrations', 'showmigrations', 'dbshell', 'flush']
    
    if command not in valid_commands:
        print(f"Invalid database command. Valid options: {', '.join(valid_commands)}")
        return
    
    execute_from_command_line(['manage.py', command])


if __name__ == '__main__':
    setup_django_environ()
    
    if not check_environment():
        sys.exit(1)
    
    main()


// === ARCHIVO: api/models/transaction.py ===
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

```
