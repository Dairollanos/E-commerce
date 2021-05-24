from decimal import Decimal
from django.conf import settings
from tienda.models import Producto

class Cart(object):
    
    def __init__(self, request):
        """
       Inicializar el carrito
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Guardar un carrito vacio en la sesion
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        # store current applied coupon
        self.cupon_id = self.session.get('cupon_id')

    def add(self, product, quantity=1, override_quantity=False):
        """
        Añadir un producto al carrito
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'cantidad': 0,'precio': str(product.precio)}
        if override_quantity:
            self.cart[product_id]['cantidad'] = quantity
        else:
            self.cart[product_id]['cantidad'] += quantity
        self.save()

    def save(self):
        # Marca la session como modificada para asegurar de que sea guardada
        self.session.modified = True
        
    def remove(self, product):
        """
        Elimina un producto del carrito
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        """
        Itera sobre los productos en el carrito y obtiene el producto 
        de la base de datos.
        """
        product_ids = self.cart.keys()
        # obtiene el objeto producto y añadelo al carrito
        products = Producto.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['precio'] = Decimal(item['precio'])
            item['total_precio'] = item['precio'] * item['cantidad']
            yield item

    
    def __len__(self):
        """
        Cuenta todos los elementos del carrito
        """
        return sum(item['cantidad'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.cart.values())

    def clear(self):
        # Remueve la sesion del carrito
        del self.session[settings.CART_SESSION_ID]
        self.save()

