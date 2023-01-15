from django.db import models
from seller.models import Seller
from customer.models import Customer

def user_directory_path_2d(instance):
    return '2Dseller_{0}/{1}-{2}'.format(instance.seller, instance.name, instance.barcode)


def user_directory_path_3d(instance):
    return '3Dseller_{0}/{1}-{2}'.format(instance.seller, instance.name, instance.barcode)

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    total_price = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=70)
    barcode = models.CharField(max_length=12)
    short_descr = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    img_2d = models.ImageField(upload_to = user_directory_path_2d)
    img_3d = models.ImageField(upload_to = user_directory_path_3d)
    size = models.CharField(max_length=20)
    stock = models.IntegerField()
    price = models.IntegerField()

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    billing = models.CharField(max_length=300)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_shipped = models.BooleanField(default=False)

