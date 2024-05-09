from django.db import models

# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)

class asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default='')
    numeroHoras = models.IntegerField(default=0)
    persona = models.ForeignKey(persona, on_delete = models.CASCADE) 
    