
# -*- coding: utf-8 -*-
from django.db import models

class Vehiculo(models.Model):
    """The base model"""
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)


    class Meta:
        abstract = True
