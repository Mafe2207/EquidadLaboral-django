from django.shortcuts import render
from django.http import HttpResponse #modulo de respuestas 

# Aqui estan las vistas de la aplicacion Create your views here.
def saludo(request):
    return render(request,"Login/home.html")

def ventas(request):
    return render(request,"Login/ventas.html" )
