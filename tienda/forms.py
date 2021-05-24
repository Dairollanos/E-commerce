from django import forms
from django.forms import fields
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    imagen = forms.ImageField(label=('Producto_Imagen'),required=True, error_messages = {'invalido':("Archivos tipo imagen solamente")}, widget=forms.FileInput)
    class Meta:
        model = Producto
        fields = ['nombre','categoria','imagen','descripcion','precio']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre',]