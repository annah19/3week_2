from django.db import models


# Stuff like nintendo, sony, sega, etc
class ProductManufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Stuff like game, console, etc
class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    cover_image = models.CharField(max_length=1024, blank=True)
    manufacturer = models.ForeignKey(ProductManufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=999, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
