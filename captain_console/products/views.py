from django.shortcuts import render, get_object_or_404
from products.models import Product

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam interdum vulputate suscipit. Ut condimentum ligula nulla, dictum blandit quam finibus a. Donec gravida elementum ipsum. Nunc ullamcorper feugiat eros, condimentum condimentum leo elementum in. Quisque magna arcu, euismod eget pharetra sed, lobortis quis ex. In placerat interdum tellus, nec mollis enim viverra vestibulum. Phasellus eget rutrum erat.
<br />
Cras eget ultricies ipsum. Curabitur viverra purus in finibus pellentesque. Mauris iaculis velit non venenatis tempor. Nunc dignissim lorem rutrum diam gravida, ac fermentum felis faucibus. Sed imperdiet nec nisl in malesuada. Praesent eget fringilla sem. Praesent consectetur malesuada sapien, et aliquam augue aliquam ac. Proin et libero facilisis nibh fermentum rutrum at a magna. Sed nunc dui, sodales ultricies nibh eu, dictum vulputate sapien. Maecenas feugiat id dolor sed tristique. Mauris semper lacus et sapien sodales, placerat iaculis nibh gravida."""

manufacturers = [
    {'id': 0, 'name': 'All'},
    {'id': 1, 'name': 'Nintendo'},
    {'id': 2, 'name': 'Playstation'}
]

categories = [
    {'id': 1, 'name': 'Game'},
    {'id': 2, 'name': 'Console'}
]

def index(request):

    selected_manufacturer = (request.GET.get("manufacturer", ""))
    selected_category = (request.GET.get("category", ""))

    games = {}
    if(selected_manufacturer != ""):
        # allir leikir sem nintendo selur
        games = Product.objects.filter(manufacturer__name__icontains=selected_manufacturer)
    if (selected_category != ""):
        games = Product.objects.filter(category__name__icontains=selected_category)


    #products_search_results = render(request, 'products/products_search_results.html', context={"products":games}, content_type='application/xhtml+xml')

    return render(request, 'products/product_list.html', context={'products': games,
                                                                 'categories':categories,
                                                                 'manufacturers':manufacturers,
                                                                 'selected_manufacturer': selected_manufacturer,
                                                                 'selected_category': selected_category })


def get_product_by_id(request, id):
    context = {"product": get_object_or_404(Product, pk=id)}
    return render(request, "products/product_details.html", context)
