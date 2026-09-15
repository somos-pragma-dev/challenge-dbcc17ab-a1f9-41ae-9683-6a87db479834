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