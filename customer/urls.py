from django.urls import path

from customer.views import CreateCustomerView 

urlpatterns = [
    path('api/v1/customers/', CreateCustomerView.as_view(), name='customers_list'),

]
