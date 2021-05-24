from django import forms
from .models import Pedido

class CrearPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'apellido', 'email', 'direccion' ,'ciudad']