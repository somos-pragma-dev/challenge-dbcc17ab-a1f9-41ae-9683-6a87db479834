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