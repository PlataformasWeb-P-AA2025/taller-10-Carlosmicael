from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ambiente.models import *

# importar los formularios de forms.py
from ambiente.forms import *

# Create your views here.


def indexBarrio(request):
    parroquias = Parroquia.objects.prefetch_related('barrios').all()
    informacion_template = {'barriosParro': parroquias}
    return render(request, 'barrioIndex.html', informacion_template)


def barrios(request,id):
    barrio = BarrioCiudadela.objects.get(pk=id)
    informacion_template = {'barrio': barrio}
    return render(request, 'barrios.html', informacion_template)



def crearBarrio(request):
    print(request)
    if request.method=='POST':
        formulario = BarrioCiudadelaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(indexBarrio)
    else:
        formulario = BarrioCiudadelaForm()
    diccionario = {'formulario': formulario}
    return render(request, 'crearBarrio.html', diccionario)


def crearParroquia(request):
    print(request)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(indexBarrio)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}
    return render(request, 'crearParroquia.html', diccionario)
