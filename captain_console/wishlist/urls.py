from django.urls import path
from . import views

# From candyqueen video - testing
urlpatterns = [
    # http://localhost:8000/wishlist
    path('', views.index, name="index"),
]
