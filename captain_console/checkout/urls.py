from django.urls import path
from . import views

# From candyqueen video - testing
urlpatterns = [
    # http://localhost:8000/checkout
    path('', views.checkout, name="checkout"),
    path('payment', views.payment_info, name="payment_info"),
    path('order_review', views.order_review, name="order_review"),
    path('order_confirmation', views.order_confirmation, name="order_confirmation")
]
