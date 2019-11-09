from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^crear_vehiculo/', CreateVehiculo.as_view(), name="crear_vehiculo"),
    url(r'^update_vehiculo/(?P<pk>\d+)/$', UpdateVehiculo.as_view(), name="editar_vehiculo"),
]