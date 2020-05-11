from django.forms import ModelForm, widgets
from django import forms

from products.models import Product, ProductCategory, ProductManufacturer


class ProductCreationForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control"}),
            "description": widgets.TextInput(attrs={"class": "form-control"}),
            "category": widgets.Select(attrs={"class": "form-control"}),
            "price": widgets.NumberInput(attrs={"class": "form-control"}),
            "manufacturer": widgets.Select(attrs={"class": "form-control"}),
            "cover_image": widgets.TextInput(attrs={"class": "form-control"}),
        }


class CategoryCreationForm(ModelForm):
    class Meta:
        model = ProductCategory
        exclude = ['id']
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control"})
        }


class ManufacturerCreationForm(ModelForm):
    class Meta:
        model = ProductManufacturer
        exclude = ['id']
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control"})
        }
