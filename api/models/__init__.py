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