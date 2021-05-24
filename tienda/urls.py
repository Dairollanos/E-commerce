from django.urls import path
from .views import product_list, product_detail, crear_producto, crear_categoria, productos_por_usuario, editar_productos

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='producto_lista'),
    path('crear/', crear_producto, name='producto_crear'),
    path('crear/categoria/', crear_categoria, name='categoria_crear'),
    path('<slug:category_slug>/', product_list, name='productos_por_categoria'),
    path('<int:id>/<slug:slug>/', product_detail,name='producto_detalles'),
    path('perfil/productos/', productos_por_usuario, name="productos_por_usuario"),
    path('perfil/productos/editar/<int:id>/<slug:slug>/', editar_productos , name="producto_editar")
]