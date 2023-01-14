from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from administrator.models import Administrator
from administrator.permissions import AdministratorsPermission
from administrator.serializers import AdministratorSerializer
from seller.models import Seller
from library_manager.serializer import ProductSerializer


class AdministratorCreate(CreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = (AllowAny,)

class ValidateSeller(APIView):
    permission_classes = (IsAuthenticated, AdministratorsPermission,)
    def patch(self, request, pk, format=None):
        seller = get_object_or_404(Seller.objects.all(), id = pk)
        seller.is_valid = True
        seller.save()
        return Response({"success": "Seller '{}' is valid now".format(seller.first_name)})


