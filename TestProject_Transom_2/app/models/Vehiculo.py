
# -*- coding: utf-8 -*-
from django.db import models

class Vehiculo(models.Model):
    """The base model"""
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    modelo = models.CharField(max_length = 50)
    color = models.CharField(max_length = 50)
    marca = models.CharField(max_length = 50)
    kilometraje = models.IntegerField()
    nuevo = models.BooleanField()

    class Meta:
        abstract = True

class Avion(Vehiculo):
    id = models.AutoField(primary_key = True)
    

    def __str__(self):
        return self.modelo


class Carro(Vehiculo):
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return self.modelo
    

    
