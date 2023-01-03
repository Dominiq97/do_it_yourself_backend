from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from administrator.models import Administrator
from customer.models import Customer
from customer.permissions import CustomersPermission
from customer.serializers import CustomerSerializer, CustomerSerializer
from library_manager.models import Book
from library_manager.serializer import BookSerializer


class CreateCustomerView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = (AllowAny,)

