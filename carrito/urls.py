from django.urls import path
from .views import cart_add, cart_detail, cart_remove
app_name = 'carrito'

urlpatterns = [
    path('', cart_detail, name='carrito_detalle'),
    path('add/<int:product_id>/', cart_add, name='carrito_añadir'),
    path('remove/<int:product_id>/', cart_remove,name='carrito_eliminar'),
]