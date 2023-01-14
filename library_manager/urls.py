from django.urls import path, include
from library_manager import views


urlpatterns = [
    path('api/v1/products/<int:pk>', views.ProductAdministrator.as_view(), name='update_delete_product'),
    path('api/v1/products', views.ProductListView.as_view()),
]