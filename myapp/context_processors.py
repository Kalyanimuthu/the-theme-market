from .utils import get_or_create_cart

def cart_count(request):
    try:
        cart = get_or_create_cart(request)
        return {"cart_count": cart.items.count()}
    except:
        return {"cart_count": 0}
