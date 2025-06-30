# gestion_empresa/serializers.py

from rest_framework import serializers
from .models import Cliente, Proveedor, Producto, Pedido, Factura, FacturaDetalle

# Serializador para el modelo Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' # Incluye todos los campos del modelo

# Serializador para el modelo Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

# Serializador para el modelo Producto
class ProductoSerializer(serializers.ModelSerializer):
    # Para mostrar el nombre del proveedor en lugar de solo su ID
    id_proveedor_razon_social = serializers.ReadOnlyField(source='id_proveedor.razon_social')

    class Meta:
        model = Producto
        fields = '__all__'
        # fields = ['Codigo', 'descripcion', 'precio', 'id_proveedor', 'id_proveedor_razon_social'] # Ejemplo de campos específicos

# Serializador para el modelo Pedido
class PedidoSerializer(serializers.ModelSerializer):
    # Para mostrar el nombre del producto y el cliente
    producto_descripcion = serializers.ReadOnlyField(source='producto.descripcion')
    cliente_nombre = serializers.ReadOnlyField(source='cliente.nombre_cliente')

    class Meta:
        model = Pedido
        fields = '__all__'
        # fields = ['id_pedido', 'producto', 'producto_descripcion', 'cliente', 'cliente_nombre', 'fecha'] # Ejemplo de campos específicos

# Serializador para el modelo Factura
class FacturaSerializer(serializers.ModelSerializer):
    # Para mostrar el nombre del cliente
    cliente_nombre = serializers.ReadOnlyField(source='cliente.nombre_cliente')

    class Meta:
        model = Factura
        fields = '__all__'
        # fields = ['num', 'fecha', 'importe', 'cliente', 'cliente_nombre'] # Ejemplo de campos específicos

# Serializador para el modelo FacturaDetalle
class FacturaDetalleSerializer(serializers.ModelSerializer):
    # Para mostrar la descripción del producto y el número de factura
    producto_descripcion = serializers.ReadOnlyField(source='producto.descripcion')
    factura_numero = serializers.ReadOnlyField(source='factura.num')

    class Meta:
        model = FacturaDetalle
        fields = '__all__'
        # fields = ['ID_Detalle', 'factura', 'factura_numero', 'producto', 'producto_descripcion', 'cantidad', 'precio_unitario'] # Ejemplo de campos específicos
