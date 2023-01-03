from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from account.models import User


class Customer(User):
    user = models.OneToOneField(to=User, parent_link=True, related_name='customer', on_delete=models.CASCADE)
    
    def __str__(self):
        return super(Customer, self).__str__()
