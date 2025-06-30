# gestion_empresa/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClienteViewSet, ProveedorViewSet, ProductoViewSet,
    PedidoViewSet, FacturaViewSet, FacturaDetalleViewSet
)

# Crea un enrutador por defecto
router = DefaultRouter()

# Registra tus ViewSets con el enrutador
router.register(r'clientes', ClienteViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'facturas', FacturaViewSet)
router.register(r'facturas-detalle', FacturaDetalleViewSet)

# Las URLs generadas por el enrutador
urlpatterns = [
    path('', include(router.urls)),
]