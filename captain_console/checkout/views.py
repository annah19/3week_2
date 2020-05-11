from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from CaptainConsole.views import get_cart_items
from checkout.forms.shipping_info import ShippingForm, PaymentForm
from checkout.models import OrderInformation, OrderProduct
from products.models import Product
from user.models import Profile


@login_required
def checkout(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ShippingForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("payment_info")
    return render(request, 'checkout/checkout.html', {
        'form': ShippingForm(instance=profile)
    })


@login_required
def payment_info(request):
    if request.method == "POST":
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            request.session["card_info"] = clean_data
            return redirect("order_review")
    return render(request, 'checkout/payment.html', {"form": PaymentForm()})


@login_required
def order_review(request):
    profile, card_info, cart = compile_order_info(request)
    return render(request, 'checkout/review.html', {"shipping": profile, "card_info": card_info, "cart": cart})


def order_confirmation(request):
    profile, card_info, cart = compile_order_info(request)

    order = OrderInformation()
    order.postal_code = profile["postal_code"]
    order.city = profile["city"]
    order.country = profile["country"]
    order.name = profile["name"]
    order.address = profile["address"]
    order.order_total = cart["subtotal"]
    order.user = request.user
    order.save()

    cart_items = request.session["cart"]
    for product_id in cart_items:
        product_amount = cart_items[product_id]
        for i in range(product_amount):
            product = Product.objects.get(pk=product_id)
            ordered_product = OrderProduct()
            ordered_product.order = order
            ordered_product.product = product
            ordered_product.save()
    del request.session["cart"]
    return render(request, 'checkout/confirmation.html', {"shipping": profile, "card_info": card_info, "cart": cart})


def compile_order_info(request):
    profile = Profile.objects.filter(user=request.user) \
        .values("name", "address", "city", "country", "postal_code").first()
    card_info = request.session["card_info"]
    cart = get_cart_items(request.session)
    return profile, card_info, cart
