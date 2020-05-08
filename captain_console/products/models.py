from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

# TODO Add cover image and type
# Type would be something like "video game" or console,
# and category would be something like "Nintendo" or "Sega"
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.FloatField()

class ProductImage(models.Model):
    image = models.CharField(max_length=999, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)