from django.db import models
import products

# Create your models here.



class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=999, blank=True)
    role = models.FloatField()

class UserWishlist(models.Model):
    wishlistuser = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlistproduct = models.ForeignKey(products.models.Product, on_delete=models.CASCADE)


