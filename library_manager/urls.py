from django.urls import path, include
from library_manager import views


urlpatterns = [
    path('api/v1/books/<int:pk>', views.BookAdministrator.as_view(), name='update_delete_book'),
    path('api/v1/books', views.BookListView.as_view()),
]