from django.contrib.auth.models import User
from django.db import models
from products.models import Product
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=999, blank=True)
    email = models.CharField(max_length=255)
    role = models.FloatField(default=0)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=999)
    city = models.CharField(max_length=999)
    country = CountryField()
    postal_code = models.CharField(max_length=255)


class UserWishlist(models.Model):
    wishlist_user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlist_product = models.ForeignKey(Product, on_delete=models.CASCADE)

