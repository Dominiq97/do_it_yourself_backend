from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from administrator.models import Administrator
from administrator.permissions import AdministratorsPermission
from administrator.serializers import AdministratorSerializer
from library_manager.models import Product
from library_manager.serializer import ProductSerializer


class AdministratorCreate(CreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = (AllowAny,)

