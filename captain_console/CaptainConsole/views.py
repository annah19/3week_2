from django.shortcuts import render

# Testing -check informational.html also
computers = [
    {'id': 1, 'name': 'Gameboy', 'price': 39.99},
    {'id': 1,'name': 'Playstation1', 'price': 49.99},
    {'id': 1,'name': 'Sega', 'price': 49.99},
    {'id': 1,'name': 'Nes', 'price': 49.99},
]
games = [
    {'id': 1,'name': 'Mario Kart', 'price': 39.99},
    {'id': 1,'name': 'Donkey Kong', 'price': 49.99},
    {'id': 1,'name': 'Pacman', 'price': 49.99},
    {'id': 1,'name': 'Sonic', 'price': 49.99},
]


def index(request):
    return render(request, 'captainconsole/index.html', context={'computers': computers,'games':games} )


def faq(request):
    return render(request, 'informational/faq.html')


def about(request):
    return render(request, 'informational/about_us.html')


def cart(request):
    return render(request, 'captainconsole/cart.html')
