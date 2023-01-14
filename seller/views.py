from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Seller
from .permissions import SellerPermission
from .serializers import SellerSerializer
from library_manager.models import Product
from library_manager.serializer import ProductSerializer
from administrator.permissions import AdministratorsPermission


class SellerCreate(CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsAuthenticated, AdministratorsPermission)

