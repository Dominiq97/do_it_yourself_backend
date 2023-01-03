import random

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from account.models import User

class Administrator(User):
    user = models.OneToOneField(to=User, parent_link=True, related_name='administrator', on_delete=models.CASCADE)

    def __str__(self):
        return super(Administrator, self).__str__()



