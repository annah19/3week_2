from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Testing -check informational.html also
from CaptainConsole.forms.product_form import ProductCreationForm, ManufacturerCreationForm, CategoryCreationForm
from products.models import ProductImage, Product


def index(request):
    computers = Product.objects.filter(category__name__icontains="console")[:4]
    games = Product.objects.filter(category__name__icontains="game")[:4]

    return render(request, 'captainconsole/index.html', context={'computers': computers,'games':games} )


def faq(request):
    return render(request, 'informational/faq.html')


def about(request):
    return render(request, 'informational/about_us.html')


def cart(request):
    if "cart" not in request.session:
        return render(request, 'captainconsole/cart.html', context={"cart": []})

    cart_items = request.session["cart"]
    cart_json = []
    cart_subtotal = 0
    for product_id in cart_items:
        product_amount = cart_items[product_id]
        product = Product.objects.get(pk=product_id)
        product_price = product.price
        product_total_price = product_price * product_amount
        product_dict = {
            "cover_art": product.cover_image,
            "name": product.name,
            "amount": product_amount,
            "price": product_price,
            "total": product_total_price
        }
        cart_json.append(product_dict)
        cart_subtotal += product_total_price

    return render(request, 'captainconsole/cart.html', context={"cart": cart_json, "subtotal": cart_subtotal})


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


def remove_from_cart(request):
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


@login_required
def create_item(request):
    if request.method == "POST":
        form = ProductCreationForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST["image"], product=product)
            product_image.save()
            return redirect("create_item")
    else:
        form = ProductCreationForm()
    return render(request, "products/create_product.html", {"form": form})


@login_required
def create_manufacturer(request):
    if request.method == "POST":
        form = ManufacturerCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_manufacturer")
    else:
        form = ManufacturerCreationForm()
    return render(request, "products/create_manufacturer.html", {"form": form})


def create_category(request):
    if request.method == "POST":
        form = CategoryCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_category")
    else:
        form = ManufacturerCreationForm()
    return render(request, "products/create_category.html", {"form": form})