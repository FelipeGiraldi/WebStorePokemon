from django.urls import path
from .views import listadoProductos


urlpatterns = [
    path('productos/',listadoProductos, name = 'listadoProductos'),
]
