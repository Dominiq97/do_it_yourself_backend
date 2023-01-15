from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Administrator
from django.db import IntegrityError

class AdministratorTests(APITestCase):
    def test_create_account_success(self):
        url = reverse('create_user')
        data = {"email": "admin@admin.com",
  "password": "password12!",
  "password2": "password12!",
  "first_name": "Johnny",
  "last_name": "Doe"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Administrator.objects.count(), 1)
        self.assertEqual(Administrator.objects.get().email, 'admin@admin.com')

    def test_create_account_pass_short(self):
        url = reverse('create_user')
        data = {"email": "admin@admin1.com",
  "password": "pass",
  "password2": "pass",
  "first_name": "John",
  "last_name": "Doe"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Administrator.objects.count(), 0)

    def test_create_account_duplicates(self):
        url = reverse('create_user')
        data = {"email": "admin@admin.com",
  "password": "password12!",
  "password2": "password12!",
  "first_name": "John",
  "last_name": "Doe"}
        response1 = self.client.post(url, data, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Administrator.objects.count(), 1)

        url = reverse('create_user')
        data = {"email": "admin@admin.com",
  "password": "password12!",
  "password2": "password12!",
  "first_name": "John",
  "last_name": "Doe"}
        with self.assertRaises(Exception) as raised: 
            data.save()
        self.assertEqual(AttributeError, type(raised.exception))
