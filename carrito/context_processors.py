from .carrito import Cart

def cart(request):
    return {'cart': Cart(request)}

    