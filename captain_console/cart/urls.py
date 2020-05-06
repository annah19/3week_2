from django.urls import path
from . import views

# From candyqueen video - testing
urlpatterns = [
    # http://localhost:8000/cart
    path('', views.index, name="cart-index"),
]
