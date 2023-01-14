from django.db import models
from seller.models import Seller

class Publisher(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)


class Product(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=70)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    stock = models.IntegerField()
    price = models.IntegerField()
