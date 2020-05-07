from django.urls import path
from . import views

# From candyqueen video - testing
urlpatterns = [
    # http://localhost:8000/
    path('', views.index, name="CaptainConsole-index"),
    path('about', views.about, name="about"),
    path('faq', views.faq, name="faq"),
    path('cart', views.cart, name="cart")
]
