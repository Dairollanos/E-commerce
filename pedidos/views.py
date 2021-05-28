from django.shortcuts import render, redirect, get_object_or_404
from .models import PedidoProducto, Pedido
from tienda.models import Producto
from .forms import CrearPedidoForm
from carrito.carrito import Cart
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
import json
import weasyprint

# Create your views here.
@login_required
def crear_pedido(request):
    cart = Cart(request)
    form = CrearPedidoForm()
    return render(request,'pedidos/pedido/crear.html',{'carrito': cart, 'form': form})

@login_required
def pdf_pedidos(request, id):
    order = get_object_or_404(Pedido, id=id)
    print(order.id)
    productos = PedidoProducto.objects.filter(pedido=order.id)
    html = render_to_string('pedidos/pedido/pdf.html',{'Pedido': order, 'productos': productos})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATICFILES_DIRS[0] + 'css/pdf.css')])
    return response

def pagoCompletado(request):
    cart = Cart(request)
    body = json.loads(request.body)
    pedido = Pedido.objects.create(nombre=request.user,productos=body['Productos'],pedidoID=body['Data']['orderID'],total=body['Total'])
    for item in cart:
        PedidoProducto.objects.create(pedido=pedido,producto=item['product'],precio=item['precio'],cantidad=item['cantidad'])
    cart.clear()
    return JsonResponse('Pago completado', safe=False)

def pedidosusuarios(request):
    pedidos = Pedido.objects.filter(nombre=request.user)
    prd = Producto.objects.get(id=1)
    prd2 = prd.pedido_items.all()
    print(prd2)
    return render(request, 'pedidos/pedido/pedidos_usuario.html', {'Pedidos': pedidos})

def detalles_pedidosusuarios(request, id):
    pedido = Pedido.objects.get(id=id)
    return render(request, 'pedidos/pedido/detalles_pedidos_usuario.html', {'Pedido': pedido})

