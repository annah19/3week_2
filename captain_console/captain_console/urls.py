"""captain_console URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CaptainConsole/', include('CaptainConsole.urls')),
    path('manufacturers/', include('manufacturer.urls')),
    path('products/', include('products.urls')),
    path('user/', include('user.urls')),
    path('cart/', include('cart.urls')),
    path('loginandregister/', include('loginandregister.urls')),
    path('checkout/', include('checkout.urls')),
    path('payment/', include('payment.urls')),
    path('review/', include('review.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('confirm/', include('confirm.urls')),
    path('info/', include('info.urls')),
    path('faq/', include('faq.urls'))


]
