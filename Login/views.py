from django.shortcuts import render
from django.http import HttpResponse #modulo de respuestas 

# Aqui estan las vistas de la aplicacion Create your views here.
def home(request):
    return render(request,"Login/home.html")

def servicios(request):
    return render(request,"Login/servicios.html" )

def tienda(request):
    return render(request,"Login/tienda.html")

def blog(request):
    return render(request,"Login/blog.html" )

def contacto(request):
    return render(request,"Login/contacto.html" )