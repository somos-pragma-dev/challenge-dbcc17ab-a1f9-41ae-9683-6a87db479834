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