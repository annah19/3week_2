from django.shortcuts import render, get_object_or_404
from products.models import Product

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam interdum vulputate suscipit. Ut condimentum ligula nulla, dictum blandit quam finibus a. Donec gravida elementum ipsum. Nunc ullamcorper feugiat eros, condimentum condimentum leo elementum in. Quisque magna arcu, euismod eget pharetra sed, lobortis quis ex. In placerat interdum tellus, nec mollis enim viverra vestibulum. Phasellus eget rutrum erat.
<br />
Cras eget ultricies ipsum. Curabitur viverra purus in finibus pellentesque. Mauris iaculis velit non venenatis tempor. Nunc dignissim lorem rutrum diam gravida, ac fermentum felis faucibus. Sed imperdiet nec nisl in malesuada. Praesent eget fringilla sem. Praesent consectetur malesuada sapien, et aliquam augue aliquam ac. Proin et libero facilisis nibh fermentum rutrum at a magna. Sed nunc dui, sodales ultricies nibh eu, dictum vulputate sapien. Maecenas feugiat id dolor sed tristique. Mauris semper lacus et sapien sodales, placerat iaculis nibh gravida."""

games = [
    {'id': 1, 'name': 'Mario Kart', 'price': 39.99, "description": lorem},
    {'id': 1, 'name': 'Donkey Kong', 'price': 49.99, "description": lorem},
    {'id': 1, 'name': 'Pacman', 'price': 49.99, "description": lorem},
    {'id': 1, 'name': 'Sonic', 'price': 49.99, "description": lorem},
]


def index(request):
    return render(request, 'products/product_list.html')


def get_product_by_id(request, id):
    # context = {"product": get_object_or_404(Product, pk=id)}
    context = {"product": games[id]}
    return render(request, "products/product_details.html", context)
