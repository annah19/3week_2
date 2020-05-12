from django.urls import path
from . import views

# From candyqueen video - testing
urlpatterns = [
    # http://localhost:8000/products
    path('', views.index, name="products-index"),
    path("<int:product_id>", views.get_product_by_id, name="product_details"),
]
