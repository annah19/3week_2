from django.shortcuts import render

# Testing -Not supposed to be here, check informational.html also
captainconsole = [
    {'name':'Gameboy','price': 39.99},
    {'name':'Gameboy','price': 49.99},
]


def index(request):
    return render(request,'captainconsole/index.html', context={'captainconsole': captainconsole})


def faq(request):
    return render(request, 'informational/faq.html')


def about(request):
    return render(request, 'informational/about_us.html')


def cart(request):
    return render(request, 'captainconsole/cart.html')