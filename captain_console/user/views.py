from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,'user/profile.html')

def wishlist(request):
    return render(request, "user/wishlist.html")
