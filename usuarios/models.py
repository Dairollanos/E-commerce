from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
opciones = (
    ('Vendedor','Vendedor'),
    ('Comprador', 'Comprador')
)

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=200, choices=opciones)
    email = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, blank=True ,null=True)
    descripcion = models.TextField(blank=True, null=True)
    contacto = models.PositiveBigIntegerField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario.username


    @receiver(post_save, sender=User)
    def post_save_create_perfil(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(usuario = instance, email= instance.email, tipo= instance.first_name)
