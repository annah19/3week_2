from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# From candyqueen video - testing
urlpatterns = [
    # http://localhost:8000/user
    path('', views.profile, name="profile"),
    path('profile', views.profile, name="profile"),
    path('wishlist', views.wishlist, name="wishlist"),
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout')
]
