
from django.urls import path
from .views import vehiculo_list, fotografia_list, vehicle_detail

urlpatterns = [
    path('veh/', vehiculo_list),
    path('foto/', fotografia_list),
    path('detail/<int:pk>/', vehicle_detail),
] 