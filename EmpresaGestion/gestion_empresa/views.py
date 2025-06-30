# gestion_empresa/views.py

from rest_framework import viewsets
from .models import Cliente, Proveedor, Producto, Pedido, Factura, FacturaDetalle
from .serializers import (
    ClienteSerializer, ProveedorSerializer, ProductoSerializer,
    PedidoSerializer, FacturaSerializer, FacturaDetalleSerializer
)

# ViewSet para Cliente: Permite operaciones CRUD (Crear, Leer, Actualizar, Borrar)
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all() # Define el conjunto de datos a usar
    serializer_class = ClienteSerializer # Define el serializador para este ViewSet

# ViewSet para Proveedor
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

# ViewSet para Producto
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# ViewSet para Pedido
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# ViewSet para Factura
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

# ViewSet para FacturaDetalle
class FacturaDetalleViewSet(viewsets.ModelViewSet):
    queryset = FacturaDetalle.objects.all()
    serializer_class = FacturaDetalleSerializer