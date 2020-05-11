from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField

from products.models import Product


class OrderInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=999)
    city = models.CharField(max_length=999)
    country = CountryField()
    postal_code = models.CharField(max_length=255)
    order_total = models.FloatField()


class OrderProduct(models.Model):
    order = models.ForeignKey(OrderInformation, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)