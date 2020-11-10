from django.shortcuts import render,redirect
from .forms import ContactoForm

def index(request):
    return render(request, 'index.html', {})


def index1(request):
    return render(request, "Web/web.html")


def crearContacto(request):
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
        return redirect('Web')
    else:
        contacto_form = ContactoForm()
    return render(request,'Web/contacto.html',{'contacto_form':contacto_form})

