"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import *
from .forms import *
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

class CreateVehiculo(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'app/create_vehiculo.html'
    success_url = reverse_lazy('home')


class ListVehiculo(UpdateView):
    model = Vehiculo
    template_name =  'app/show_vehiculo.html'

class UpdateVehiculo(UpdateView):
    model = Vehiculo
    template_name = 'aplication/update_vehiculo.html'
    success_url = reverse_lazy('home')


