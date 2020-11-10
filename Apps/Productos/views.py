from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto
from Apps.cart.cart import Cart



@login_required(login_url='autenticacion/acceder')
def listadoProductos(request):
    cart = Cart(request)
    producto = Producto.objects.all()
    return render(request, "Productos/listado.html",{"Producto":producto})


