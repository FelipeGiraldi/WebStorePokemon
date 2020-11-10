from django.urls import path
from .views import crearContacto


urlpatterns =[
    path('contacto/',crearContacto, name = 'contacto')

]