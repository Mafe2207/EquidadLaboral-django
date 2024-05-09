from django.urls import path
from Login.views import saludo 
from ventas.views import ventas 

urlpatterns = [
    path('', saludo),
    path('vent/', ventas),
]
  