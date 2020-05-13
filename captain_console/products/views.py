from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from products.forms.update_form import ProductUpdateForm
from products.models import Product, ProductCategory, ProductManufacturer
from user.views import is_user_staff


def index(request):
    manufacturer = request.GET.get("manufacturer", "")
    category = request.GET.get("category", "")
    search = request.GET.get("search", "")
    order_by = request.GET.get("order_by", "name")

    if search == "":
        games = Product.objects.filter(manufacturer__name=manufacturer, category__name__icontains=category)
    else:
        games = Product.objects.filter(name__icontains=search)
        add_to_search_history(request, search)
    print(order_by)
    if order_by == "name" or order_by == "price":
        games = games.order_by(order_by)
    search_history = get_search_history(request)
    return render(request, 'products/product_list.html', context={'products': games,
                                                                  'categories': ProductCategory.objects.all(),
                                                                  'manufacturers': ProductManufacturer.objects.all(),
                                                                  'selected_manufacturer': manufacturer,
                                                                  'selected_category': category,
                                                                  'selected_order_by': order_by,
                                                                  'search_history': search_history
                                                                  })


def get_product_by_id(request, product_id):
    context = {"product": get_object_or_404(Product, pk=product_id), "is_staff": is_user_staff(request)}
    return render(request, "products/product_details.html", context)


def add_to_search_history(request, search):
    if search != "":
        if "search_history" not in request.session:
            request.session["search_history"] = []
        request.session["search_history"].append(search)
        request.session.modified = True


def get_search_history(request):
    if "search_history" not in request.session:
        request.session["search_history"] = []
    return request.session["search_history"]


def update_product(request, product_id):
    instance = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("product_details", product_id=product_id)
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, "products/update_product.html", {
        "form": form,
        "id": product_id
    })