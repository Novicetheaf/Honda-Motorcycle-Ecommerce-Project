from django.shortcuts import get_object_or_404
from motorcycles.models import Motorcycle


def cart_contents(request):
    """
    Ensures that the cart contents are available upon rendering every page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        motorcycle = get_object_or_404(Motorcycle, pk=id)
        total += quantity * motorcycle.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'motorcycle': motorcycle})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
