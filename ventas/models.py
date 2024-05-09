from django.db import models

# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    