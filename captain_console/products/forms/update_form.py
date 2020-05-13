from django.forms import ModelForm

from products.models import Product


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['id']
