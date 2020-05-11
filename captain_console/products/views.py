from django.shortcuts import render, get_object_or_404
from products.models import Product, ProductCategory, ProductManufacturer


def index(request):
    manufacturer = (request.GET.get("manufacturer", ""))
    category = (request.GET.get("category", ""))
    search = request.GET.get("search", "")

    games = {}
    if search == "":
        games = Product.objects.filter(manufacturer__name__icontains=manufacturer, category__name__icontains=category)
    else:
        games = Product.objects.filter(name__icontains=search)

    return render(request, 'products/product_list.html', context={'products': games,
                                                                  'categories': ProductCategory.objects.all(),
                                                                  'manufacturers': ProductManufacturer.objects.all(),
                                                                  'selected_manufacturer': manufacturer,
                                                                  'selected_category': category})


def get_product_by_id(request, product_id):
    context = {"product": get_object_or_404(Product, pk=product_id)}
    return render(request, "products/product_details.html", context)
