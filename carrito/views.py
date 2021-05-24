from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from tienda.models import Producto
from .carrito import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['cantidad'],override_quantity=cd['sobreescribir'])
    return redirect('carrito:carrito_detalle')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, id=product_id)
    cart.remove(product)
    return redirect('carrito:carrito_detalle')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'cantidad': item['cantidad'],'sobreescribir': True})
    return render(request, 'carrito/detalle.html', {'cart': cart})