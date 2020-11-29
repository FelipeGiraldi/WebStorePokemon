"""WebStorePokemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Apps.Orden.views import OrderDetail, OrderList, process_order
from Apps.Orden import views
from Apps.Productos.views import listadoProductos
from django.contrib import admin
from django.urls import path, include
from Apps.Web.views import crearContacto, index
from Apps.Autenticacion.views import vistaRegistro,salir,acceder
from Apps.Web.views import index1
from Apps.cart.views import AgregarProducto, DecrementarProducto, EliminarProducto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name = 'index'),
    path('acceder/',acceder, name = 'acceder'),
    path('registro/',vistaRegistro.as_view(), name = 'vistaRegistro'),
    path('salir/',salir, name = 'salir'),
    path('web/',index1, name = 'Web'),
    path('contacto/',crearContacto, name = 'Web'),
    path('productos/',listadoProductos, name = 'listadoProductos'),
    path('cart/', include('Apps.cart.urls')),
    path('AgregarProducto/',AgregarProducto, name = 'AgregarProducto'),
    path('DecrementarProducto/',DecrementarProducto, name = 'DecrementarProducto'),
    path('EliminarProducto/',EliminarProducto, name = 'EliminarProducto'),
    path('process_order/',process_order, name = 'process_order'),
    path('listadoOrden/',OrderList.as_view(), name = 'listadoOrden'),
    path('detalle/<int:pk>/',views.Order, name = 'detalle'),
    

]
