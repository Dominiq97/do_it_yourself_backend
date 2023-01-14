from django.urls import path, re_path

from administrator.views import AdministratorCreate, ValidateSeller

urlpatterns = [
    path('api/v1/administrators', AdministratorCreate.as_view(), name='create_user'),
    path('api/v1/administrators/validate_seller/<str:pk>/', ValidateSeller.as_view(), name='validate_seller'),
]
