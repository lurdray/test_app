# test_app/custom_user/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from custom_user.models import CustomUser

class UserAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(
            first_name="first_name",
            last_name="last_name",
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )
        self.user_id = self.user.id

    def test_sign_up(self):
        url = reverse('custom_user:sign_up')
        data = {
            "first_name": "first name",
            "last_name": "last_name",
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_sign_in(self):
        url = reverse('custom_user:sign_in')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_users(self):
        url = reverse('custom_user:all')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        url = reverse('custom_user:update_user', args=[self.user_id])
        data = {
            "first_name": "new first name",
            "last_name": "last name",
            "email": "newemail@gmail.com"
            }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        url = reverse('custom_user:delete_user', args=[self.user_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_user_detail(self):
        url = reverse('custom_user:get_user_detail', args=[self.user_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_balance(self):
        url = reverse('custom_user:get_balance', args=[self.user_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_transaction_to_user(self):
        url = reverse('custom_user:add_transaction_to_user', args=["bf306b73-9805-4774-956b-9002323eadb4",])
        data = {
            "sender": "fourier",
            "receiver": "ray",
            "amount": 10,
            "status": True,
            "pub_date": "2024-10-22T08:46:10.720Z"
            }
        response = self.client.post(url, data)
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# To run the tests, use the following command in your terminal:
# python manage.py test test_app.custom_user


import unittest
import requests

class TestTransactionsEndpoint(unittest.TestCase):
    
    BASE_URL = "http://localhost:8000/transaction/transaction/"  # Update with your actual base URL

    def test_get_transactions(self):
        """Test retrieving transactions."""
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)  # Expecting a list of transactions

    def test_create_transaction(self):
        """Test creating a new transaction."""
        new_transaction = {
            "amount": 100.0,
            "sender": "sender",
            "receiver": "receiver"
        }
        response = requests.post(self.BASE_URL, json=new_transaction)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())  # Check if the response contains an ID

if __name__ == "__main__":
    unittest.main()