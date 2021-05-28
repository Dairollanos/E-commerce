from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Perfil

opciones = (
    ('Vendedor','Vendedor'),
    ('Comprador', 'Comprador')
)

class RegistrarUsuarioForm(UserCreationForm):
    tipo = forms.ChoiceField(required=True, choices=opciones)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['email','direccion','tipo', 'descripcion', 'contacto']