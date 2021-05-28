from django.urls import path
from .views import crear_pedido, pdf_pedidos, pagoCompletado, pedidosusuarios, detalles_pedidosusuarios

app_name = 'pedidos'

urlpatterns = [
    path('crear/', crear_pedido, name='pedido_crear'),
    path('<int:id>/pdf/', pdf_pedidos, name='pedido_pdf'),
    path('completado/', pagoCompletado , name='pedido_completado'),
    path('perfil/pedidos/', pedidosusuarios , name='pedidos_usuario'),
    path('perfil/pedidos/<int:id>/', detalles_pedidosusuarios , name='detalles_pedidos_usuario'),
]