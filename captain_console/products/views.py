from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from products.models import Product, ProductCategory, ProductManufacturer


def index(request):
    manufacturer = request.GET.get("manufacturer", "")
    category = request.GET.get("category", "")
    search = request.GET.get("search", "")
    order_by = request.GET.get("order_by", "name"),




    games = {}
    if search == "":
        games = Product.objects.filter(manufacturer__name__icontains=manufacturer, category__name__icontains=category)
    else:
        games = Product.objects.filter(name__icontains=search)

    if order_by == "name" or order_by == "price":
        games = games.order_by(order_by)

    return render(request, 'products/product_list.html', context={'products': games,
                                                                  'categories': ProductCategory.objects.all(),
                                                                  'manufacturers': ProductManufacturer.objects.all(),
                                                                  'selected_manufacturer': manufacturer,
                                                                  'selected_category': category,
                                                                  'selected_order_by': order_by
                                                                  })


def get_product_by_id(request, product_id):
    context = {"product": get_object_or_404(Product, pk=product_id)}
    return render(request, "products/product_details.html", context)

def add_to_search_history(request):
    search = request.GET.get("search", "")

    if search == "":

        search_id = 0
        if "search_history" in request.session:
            if search_id in request.session["search_history"]:
                request.session["search_history"][search_id] += 1
            else:
                request.session["cart"][search_id] = 1
        else:
            request.session["search_history"] = {}
            request.session["cart"][search_id] = 1
        request.session.modified = True
        return JsonResponse({"data": request.session["search_history"]})

'''def get_search_history(session):
    if "search_history" not in session:
        return {"search_history": [], "queries": 0}
    search_quries = session["search_history"]
    search_history_response = []
    queries = 0
    for product_id in search_quries:
        searches = search_quries[search_id]
        id = Product.objects.get(pk=search_id)

        search_dict = {}
        search_history_response.append(search_dict)
        queries += product_total_price
    return {"cart": cart_response, "subtotal": cart_subtotal}'''


