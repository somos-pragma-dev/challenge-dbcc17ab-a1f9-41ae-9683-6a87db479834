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