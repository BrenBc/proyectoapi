from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .models import Vehiculo, Fotografia
from .serializers import VehiculoSerializer, FotografiaSerializer
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def vehiculo_list(request):
    if request.method == 'GET':
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def fotografia_list(request):
    if request.method == 'GET':
        foto = Fotografia.objects.all()
        serializer = FotografiaSerializer(foto, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def vehicle_detail(request, pk):
    try:
        vehiculo= Vehiculo.objects.get(pk=pk)
    except Vehiculo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
       
        serializer = VehiculoSerializer(vehiculo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(vehiculo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)