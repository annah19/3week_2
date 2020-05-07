from django.urls import path
from . import views

# From candyqueen video - testing
urlpatterns = [
    # http://localhost:8000/user
    path('', views.profile, name="profile"),
    path('wishlist', views.wishlist, name="wishlist")
]
