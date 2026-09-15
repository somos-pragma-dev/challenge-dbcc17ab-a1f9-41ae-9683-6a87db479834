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