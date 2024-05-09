from django.shortcuts import render
from django.http import HttpResponse #modulo de respuestas 

# Aqui estan las vistas de la aplicacion Create your views here.
def ventas (request):
    return HttpResponse("<H1> Estas en la seccion de ventas")

# Create your views here.
