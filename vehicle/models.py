from django.db import models

# Create your models here.
class Categoria(models.Model):
    tipo_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_categoria
    


class Combustible(models.Model):
    tipo_combustible = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_combustible

class Estado(models.Model):
    tipo_estado = models.CharField(max_length=100) 

    def __str__(self):
        return self.tipo_estado

class ProveedorManager(models.Manager):
    def get_by_natural_key(self, proveedor):
        return self.get(proveedor=proveedor)


class Proveedor(models.Model):
    objects = ProveedorManager()
    proveedor = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.proveedor
    
    class Meta:
        ordering = ['proveedor']

    

    def natural_key(self):
        return (self.proveedor)

class Vehiculo(models.Model):
    color = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    kilometraje= models.IntegerField()
    precio = models.FloatField()
    puja = models.FloatField()
    categoria = models.ForeignKey(Categoria,  on_delete=models.CASCADE)
    combustible = models.ForeignKey(Combustible,  on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,  on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor,  on_delete=models.CASCADE)


    def __str__(self):
        return '%s' % (self.marca)
        

class Fotografia(models.Model):
    fotografia = models.ImageField(blank=True, null=True)
    vehiculo = models.ForeignKey(Vehiculo, related_name='imagenes', on_delete=models.CASCADE)

    def __str__(self):
        return self.fotografia.url

class Puja(models.Model):
    monto_puja = models.FloatField()
    fecha_puja = models.DateTimeField()
    vehiculo_puja = models.ForeignKey(Vehiculo, related_name='aumento_precio', on_delete=models.CASCADE)
    cliente = models.IntegerField()

    def __str__(self):
        return str(self.monto_puja)

class Transaccion(models.Model):
    precio_vehiculo = models.FloatField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    vehiculo_transaccion = models.ForeignKey(Vehiculo, related_name='transaccion_veh', on_delete=models.CASCADE )
    puja = models.ForeignKey(Puja, related_name='trans_puja', on_delete=models.CASCADE)
    cliente = models.IntegerField()


