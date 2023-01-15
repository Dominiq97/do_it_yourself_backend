import logging
import sqlite3
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer
from django.db import IntegrityError

class CustomerTests(APITestCase):
    def test_create_account_success(self):
        url = reverse('customers_list')
        data = {"email": "customer@simple.com",
  "password": "password12!",
  "password2": "password12!",
  "first_name": "John",
  "last_name": "Doe"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().email, 'customer@simple.com')

    def test_create_account_pass_short(self):
        url = reverse('customers_list')
        data = {"email": "customer@simple.com",
  "password": "pass",
  "password2": "pass",
  "first_name": "John",
  "last_name": "Doe"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Customer.objects.count(), 0)

    def test_create_account_duplicates(self):
        url = reverse('customers_list')
        data = {"email": "customer@simple.com",
  "password": "password12!",
  "password2": "password12!",
  "first_name": "John",
  "last_name": "Doe"}
        response1 = self.client.post(url, data, format='json')

        url = reverse('customers_list')
        data = {"email": "customer@simple.com",
  "password": "password12!",
  "password2": "password12!",
  "first_name": "John",
  "last_name": "Doe"}
        with self.assertRaises(Exception) as raised:  # top level exception as we want to figure out its exact type
            data.save()
        self.assertEqual(AttributeError, type(raised.exception))
        # self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Customer.objects.count(), 1)
