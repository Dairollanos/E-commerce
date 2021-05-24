from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def save(self, *args, **kwargs):
            if not self.id:
                self.slug = slugify(self.nombre)

            super(Categoria, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tienda:productos_por_categoria', args=[self.slug])


    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d',blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nombre',)
        index_together = (('id', 'slug'),)

    def save(self, *args, **kwargs):
            if not self.id:
                self.slug = slugify(self.nombre)

            super(Producto, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tienda:producto_detalles', args=[self.id, self.slug])

    def __str__(self):
        return self.nombre