"""mitienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy, re_path
from usuarios.views import login_view, logout_view, registrar_view, perfil_view

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('registrar/', registrar_view, name = "registrar"),
    path('perfil/', perfil_view, name="perfil" ),
    path('carrito/', include('carrito.urls', namespace='carrito')),
    path('', include('tienda.urls', namespace='tienda')),
    path('pedidos/', include('pedidos.urls', namespace='pedidos')),
    path('cambiar_contraseña/',auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('cambiar_contraseña_hecho')),name='cambiar_contraseña'),
    path('cambiar_contraseña/hecho/',auth_views.PasswordChangeDoneView.as_view(),name='cambiar_contraseña_hecho'),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)