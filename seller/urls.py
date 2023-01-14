from django.urls import path

from .views import SellerCreate #AdministratorTripsList #AdministratorsListView, StartTripView, EndTripView, 

urlpatterns = [
    path('api/v1/seller', SellerCreate.as_view(), name='create_user'),
]
