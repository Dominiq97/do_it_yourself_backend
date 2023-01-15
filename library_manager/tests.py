from django.test import TestCase
from .models import Product
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from seller.models import Seller
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework import status
# Include an appropriate `Authorization:` header on all requests.

class SimpleTestDetail(TestCase):
    def test_product(self):
        client = APIClient()
        client.get('/api/v1/products/', {'name': 'scaun'}, format='json')
        client.get('/api/v1/seller/', {'name': 'scaun'}, format='json')
        client.get('/api/v1/customers/', {'name': 'scaun'}, format='json')
        client.get('/api/v1/administrators/', {'name': 'scaun'}, format='json')

    def test_product(self):
        client = APIClient()
        client.get('/api/v1/products/', {'name': 'scaun'}, format='json')
        client.get('/api/v1/seller/', {'name': 'scaun'}, format='json')
        client.get('/api/v1/customers/', {'name': 'scaun'}, format='json')
        client.get('/api/v1/administrators/', {'name': 'scaun'}, format='json')

    def test_auth(self):
        client = APIClient()
        client.login(username='lauren', password='secret')
        factory = APIRequestFactory()
        request = factory.post('/api/v1/products/', {'title': 'new idea'})

