from django.contrib.auth.models import User
from django.db import models
from products.models import Product

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #favorite_product = models.ForeignKey(Product, on_delete= models.CASCADE)
    profile_image= models.CharField(max_length=999)
'''class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=999, blank=True)
    role = models.FloatField()

class UserWishlist(models.Model):
    wishlistuser = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlistproduct = models.ForeignKey(products.models.Product, on_delete=models.CASCADE)'''


# When you re-insert the classes remember to run "python manage.py makemigrations" in terminal
# Then "python manage.py migrate"