from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.FloatField()

class ProductImage(models.Model):
    image = models.CharField(max_length=999, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)