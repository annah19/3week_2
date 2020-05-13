from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from checkout.models import OrderInformation
from user.forms.profile_form import ProfileForm
from user.models import Profile


# @login_required
# def wishlist(request):
#     return render(request, "user/wishlist.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile), 'is_staff': is_user_staff(request)
    })


def is_user_staff(request):
    if not request.user.is_authenticated:
        return 0
    profile_maybe = Profile.objects.filter(user=request.user).first()
    if profile_maybe is None:
        return 0
    return profile_maybe.role
