from django.shortcuts import render
from .models import Producto
from Apps.cart.cart import Cart




def listadoProductos(request):
    cart = Cart(request)
    producto = Producto.objects.all()
    return render(request, "Productos/listado.html",{"Producto":producto})


