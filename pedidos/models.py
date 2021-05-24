from django.db import models
from tienda.models import Producto
from django.urls import reverse
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Pedido(models.Model):
    nombre = models.CharField(max_length=50)
    productos = models.CharField(max_length=500)
    pedidoID = models.CharField(max_length=250, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, default=1)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    pago = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    descuento = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])

    class Meta:
        ordering = ('-creado',)
        verbose_name = 'Pedido'

    def __str__(self):
        return f'Pedido {self.id}'

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.descuento / Decimal(100))

    def get_absolute_url(self):
        return reverse('pedidos:pedido_pdf', kwargs={'id': self.id})

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido,related_name='items',on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,related_name='pedido_items',on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.precio * self.cantidad