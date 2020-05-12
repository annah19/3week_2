from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from products.models import Product, ProductCategory, ProductManufacturer


def index(request):
    manufacturer = request.GET.get("manufacturer", "")
    category = request.GET.get("category", "")
    search = request.GET.get("search", "")
    order_by = request.GET.get("order_by", "name")

    if search == "":
        games = Product.objects.filter(manufacturer__name__icontains=manufacturer, category__name__icontains=category)
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
    context = {"product": get_object_or_404(Product, pk=product_id)}
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
