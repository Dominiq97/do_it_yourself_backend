from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.views import APIView
from library_manager.models import Product
from rest_framework.parsers import JSONParser
from library_manager.serializer import ProductSerializer, ProductRegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from administrator.permissions import AdministratorsPermission
from customer.permissions import CustomersPermission
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.decorators import action
title = openapi.Parameter('title', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING)

FETCH_PUBLISHER_SUCCESS = '''{{
    "name": <publisher name>,
    "address": <publisher address>,
    "product": [
        {
            "title": <product name>,
            "publisher": <publisher id>
        }
    ]
}}'''

FETCH_BOOK_SUCCESS = '''{{
    "title": <product title>,
    "author": <product author>,
}}'''


class ProductAdministrator(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, AdministratorsPermission]

    def delete(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return Response({"status": "success", "data": "Product Deleted"})
        
    def put(self, request, pk):
        product = get_object_or_404(Product.objects.all(), id = pk)
        data = request.data.get('product')
        serializer = ProductSerializer(instance=product, data=data, partial=True)
        if serializer.is_valid():
            product = serializer.save()
        return Response({"success": "Product '{}' is updated".format(product.title)})


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AdministratorsPermission|CustomersPermission,)
    def get_queryset(self):
        title = self.request.query_params.get("title", None)
        author = self.request.query_params.get("author", None)
        publisher = self.request.query_params.get("publisher", None)
        if title:
            qs = Product.objects.filter(title__icontains=title)
            return qs
        if author:
            qs = Product.objects.filter(author__icontains=author)
            return qs
        if publisher:
            qs = Product.objects.filter(publisher__name__icontains=publisher)
            return qs

        return super().get_queryset()
