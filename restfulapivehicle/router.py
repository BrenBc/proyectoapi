from vehicle.viewsets import VehiculoViewset
from vehicle.viewsets import FotografiaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('vehiculo', VehiculoViewset)
router.register('fotografia', FotografiaViewset)