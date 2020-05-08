from django.http import JsonResponse
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
    if "cart" in request.session:
        # TODO make this return cover art, name, amount, price
        # Amount is in request.session["cart"][str(product_id)]

        amount = request.session["cart"]["1"]
        temp_data = [
            {
                "cover_art": "https://upload.wikimedia.org/wikipedia/sco/6/6a/Super_Mario_64_box_cover.jpg",
                "name": "Mario 64",
                "amount": amount,
                "price": 4.99,
                "total": amount * 4.99
            },
            {
                "cover_art": "https://upload.wikimedia.org/wikipedia/en/c/c1/Kirby64_box.jpg",
                "name": "Kirby 64",
                "amount": 1,
                "price": 5.99,
                "total": 1 * 5.99
            }
        ]
        return render(request, 'captainconsole/cart.html', context={"cart": temp_data})
    return render(request, 'captainconsole/cart.html', context={"cart": []})


def add_to_cart(request):
    if request.method == "GET":
        str_id = str(request.GET["product_id"])
        if "cart" in request.session:
            if str_id in request.session["cart"]:
                request.session["cart"][str_id] += 1
            else:
                request.session["cart"][str_id] = 1
        else:
            request.session["cart"] = {}
            request.session["cart"][str_id] = 1
        request.session.modified = True
        return JsonResponse({"data": request.session["cart"]})


def remove_from_cart(request, product_id):
    if request.method == "GET":
        str_id = str(request.GET["product_id"])
        amount = int(request.GET["amount"])
        if "cart" in request.session:
            if str_id in request.session["cart"]:
                request.session["cart"][str_id] -= amount
                if request.session["cart"][str_id] <= 0:
                    del request.session["cart"][str_id]
                request.session.modified = True
        return JsonResponse({"data": request.session["cart"]})