from rest_framework import serializers
from .models import Vehiculo, Proveedor, Categoria, Combustible, Estado
from .models import Fotografia
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

#class CombustibleSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Combustible
        #fields = ('tipo_combustible')   
        

class VehiculoSerializer(serializers.ModelSerializer):
    imagenes = serializers.StringRelatedField(many=True) 
    tipo_combustible = serializers.SerializerMethodField('get_datos_combustible')
    proveedor = serializers.SerializerMethodField('get_datos_proveedor')
    tipo_estado = serializers.SerializerMethodField('get_datos_estado')
    tipo_categoria = serializers.SerializerMethodField('get_datos_categoria')
    aumento_precio = serializers.StringRelatedField(many=True)
    transaccion_veh = serializers.StringRelatedField(many=True)

    class Meta:
        model = Vehiculo
        fields = ('id', 'color', 'marca', 'kilometraje', 'precio', 'aumento_precio', 'tipo_combustible',  'tipo_categoria',  'tipo_estado', 'proveedor', 'transaccion_veh', 'imagenes', 'estado' )

    def get_datos_combustible(self, Vehiculo):
        tipo_combustible = Vehiculo.combustible.tipo_combustible
        return tipo_combustible
    
    def get_datos_proveedor(self, Vehiculo):
        proveedor = Vehiculo.proveedor.proveedor
        return proveedor

    def get_datos_estado(self, Vehiculo):
        tipo_estado = Vehiculo.estado.tipo_estado
        return tipo_estado

    def get_datos_categoria(self, Vehiculo):
        tipo_categoria = Vehiculo.categoria.tipo_categoria
        return tipo_categoria


class FotografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotografia
        fields = '__all__'



