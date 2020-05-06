from django.urls import path
from . import views

# From candyqueen video - testing
urlpatterns = [
    # http://localhost:8000/manufacturers
    path('', views.index, name="manufacturer-index"),
]
