from django.urls import path

from administrator.views import AdministratorCreate #AdministratorTripsList #AdministratorsListView, StartTripView, EndTripView, 

urlpatterns = [
    path('api/v1/administrators', AdministratorCreate.as_view(), name='create_user'),
    # path('Administrators_list/', AdministratorsListView.as_view(), name='Administrator_list'),
    # path('start_trip/', StartTripView.as_view(), name='start_trip'),
    # path('end_trip/', EndTripView.as_view(), name='end_trip'),
    # path('trips_list/', AdministratorTripsList.as_view(), name='trips_list'),

]
