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