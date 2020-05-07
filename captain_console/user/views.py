from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def profile(request):
    return render(request,'user/profile.html')

def wishlist(request):
    return render(request, "user/wishlist.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'user/register.html', {
        'form': UserCreationForm()
    })
