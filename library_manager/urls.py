from django.urls import path, include
from library_manager import views


urlpatterns = [
    path('api/v1/products/<int:pk>', views.ProductSeller.as_view(), name='update_delete_product'),
    path('api/v1/products', views.ProductListView.as_view(), name='crud_private_products'),
    path('api/v1/products/public', views.PublicProducts.as_view(), name='get_public_products'),
]