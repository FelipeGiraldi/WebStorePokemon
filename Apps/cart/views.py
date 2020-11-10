from django.shortcuts import redirect
from Apps.Productos.models import Producto
from django.contrib.auth.decorators import login_required
from .cart import Cart


@login_required(login_url="/autenticacion/login")
def AgregarProducto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.Agregar(producto=producto)
    return redirect("listadoProductos")


@login_required(login_url="/autenticacion/login")
def EliminarProducto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.Eliminar(producto)
    return redirect("listadoProductos")


@login_required(login_url="/autenticacion/login")
def DecrementarProducto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.Decrementar(producto=producto)
    return redirect("listadoProductos")


@login_required(login_url="/autenticacion/login")
def LimpiarCarrito(request):
    cart = Cart(request)
    cart.clear()
    return redirect("listadoProductos")
