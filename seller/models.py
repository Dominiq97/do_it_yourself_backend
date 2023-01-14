import random

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from account.models import User

class Seller(User):
    user = models.OneToOneField(to=User, parent_link=True, related_name='seller', on_delete=models.CASCADE)

    def __str__(self):
        return super(Seller, self).__str__()



