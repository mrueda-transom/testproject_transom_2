from django.test import TestCase
import pytest
from .models.Vehiculo import *
from types import *


def get_model_avion():
    avion = Avion()
    modelo = avion.modelo = 'Avion123'
    return modelo

def get_model_carro():
    carro = Carro()
    modelo = carro.modelo = 'Aveo 2016'
    return modelo

def get_kilometraje():
    carro = Carro()
    kilometros = carro.kilometraje = 10000
    return kilometros

def get_nuevo():
    avion = Avion()
    nuevo = avion.nuevo = True
    return nuevo


def test_vehiculo():
    assert type(get_kilometraje()) is int 
    assert type(get_nuevo()) is bool
    assert get_model_avion() != None
    assert len(get_model_carro()) < 50

