from .models import Cart
from django.utils.crypto import get_random_string

def get_or_create_cart(request):
    # ensure the session exists
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    # get or create cart
    cart, created = Cart.objects.get_or_create(session_key=session_key)

    # force session_key in case of old NULL rows
    if not cart.session_key:
        cart.session_key = session_key
        cart.save()

    return cart
