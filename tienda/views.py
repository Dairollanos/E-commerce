from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Producto
from carrito.forms import CartAddProductForm
from .forms import ProductoForm, CategoriaForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def product_list(request, category_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponible=True)
    if category_slug:
        categoria = get_object_or_404(Categoria, slug=category_slug)
        productos = productos.filter(categoria=categoria)
    context = {'Categoria': categoria,'Categorias': categorias,'Productos': productos}
    return render(request,'tienda/producto/lista.html', context)

def product_detail(request, id, slug):
    producto = get_object_or_404(Producto,id=id,slug=slug,disponible=True)
    cart_product_form = CartAddProductForm()
    context = {
        'Producto': producto,
        'CarritoForm': cart_product_form
    }
    return render(request,'tienda/producto/detalle.html', context)

@login_required
def crear_producto(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.usuario = request.user
        obj.save()
        return redirect('perfil')
    context = {
        'Form': form
    }
    return render(request, 'tienda/producto/crear.html', context)

@login_required
def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('shop:producto_crear')
    context = {
        'Form': form
    }
    return render(request, 'tienda/producto/crear_categoria.html', context)

@login_required
def productos_por_usuario(request):
    productos = Producto.objects.filter(usuario= request.user)
    return render(request, 'tienda/producto/usuario/lista.html', {'Productos': productos})

@login_required
def editar_productos(request, id, slug):
    producto = get_object_or_404(Producto,id=id,slug=slug,disponible=True)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.usuario = request.user
        obj.save()
        return redirect('perfil')
    context = {
        'Producto': producto,
        'Form': form
    }
    return render(request,'tienda/producto/usuario/editar.html', context)