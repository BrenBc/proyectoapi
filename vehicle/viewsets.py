from rest_framework import viewsets
from . import models
from . import serializers

class VehiculoViewset(viewsets.ModelViewSet):
    
    queryset = models.Vehiculo.objects.all()
    serializer_class = serializers.VehiculoSerializer

class FotografiaViewset(viewsets.ModelViewSet):

    queryset = models.Fotografia.objects.all()
    serializer_class = serializers.FotografiaSerializer