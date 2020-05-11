from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=999)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=999, blank=True)
    role = models.FloatField()


class UserWishlist(models.Model):
    wishlist_user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlist_product = models.ForeignKey(Product, on_delete=models.CASCADE)

