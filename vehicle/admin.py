from django.contrib import admin
from .models import Vehiculo, Proveedor, Categoria, Combustible, Estado
from .models import Fotografia, Puja, Transaccion

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Fotografia)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Combustible)
admin.site.register(Estado)
admin.site.register(Puja)
admin.site.register(Transaccion)