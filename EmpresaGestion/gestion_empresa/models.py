# gestion_empresa/models.py

from django.db import models

# Modelo para Clientes
class Cliente(models.Model):
    # ID se crea automáticamente como clave primaria autoincremental por defecto.
    nombre_cliente = models.CharField(max_length=50, verbose_name="Nombre Cliente")
    celular = models.CharField(max_length=80, verbose_name="Número Celular")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = 'Clientes' # Asegura que el nombre de la tabla en la BD sea 'Clientes'

    def __str__(self):
        return self.nombre_cliente

# Modelo para Proveedor
class Proveedor(models.Model):
    rut = models.IntegerField(primary_key=True, verbose_name="RUT del Proveedor")
    razon_social = models.CharField(max_length=50, verbose_name="Razón Social")
    telefono = models.CharField(max_length=80, verbose_name="Teléfono")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = 'Proveedor' # Asegura que el nombre de la tabla en la BD sea 'Proveedor'

    def __str__(self):
        return self.razon_social

# Modelo para Productos
class Producto(models.Model):
    # Codigo se crea automáticamente como clave primaria autoincremental por defecto.
    descripcion = models.CharField(max_length=50, verbose_name="Descripción")
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio")
    # Relación uno a muchos con Proveedor
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,
                                     db_column='ID_Proveedor', verbose_name="Proveedor")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = 'Productos' # Asegura que el nombre de la tabla en la BD sea 'Productos'

    def __str__(self):
        return self.descripcion

# Modelo para Pedidos
class Pedido(models.Model):
    # id_pedido se crea automáticamente como clave primaria autoincremental por defecto.
    # Relación uno a muchos con Producto
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,
                                  db_column='Codigo', verbose_name="Producto")
    # Relación uno a muchos con Cliente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,
                                db_column='ID_Cliente', verbose_name="Cliente")
    fecha = models.DateField(verbose_name="Fecha del Pedido")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        db_table = 'Pedidos' # Asegura que el nombre de la tabla en la BD sea 'Pedidos'

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre_cliente}"

# Modelo para Factura
class Factura(models.Model):
    num = models.IntegerField(primary_key=True, verbose_name="Número de Factura")
    fecha = models.DateField(verbose_name="Fecha de Factura")
    importe = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Importe Total")
    # Relación uno a muchos con Cliente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,
                                db_column='ID_Cliente', verbose_name="Cliente")

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        db_table = 'Factura' # Asegura que el nombre de la tabla en la BD sea 'Factura'

    def __str__(self):
        return f"Factura {self.num}"

# Modelo para Factura_Detalle
class FacturaDetalle(models.Model):
    # ID_Detalle se crea automáticamente como clave primaria autoincremental por defecto.
    # Relación uno a muchos con Factura
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE,
                               db_column='Num_Factura', verbose_name="Número de Factura")
    # Relación uno a muchos con Producto
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,
                                 db_column='Codigo_Producto', verbose_name="Producto")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio Unitario")

    class Meta:
        verbose_name = "Detalle de Factura"
        verbose_name_plural = "Detalles de Factura"
        db_table = 'Factura_Detalle' # Asegura que el nombre de la tabla en la BD sea 'Factura_Detalle'
        # Añade una restricción de unicidad para evitar duplicados en el detalle de una factura
        unique_together = ('factura', 'producto')

    def __str__(self):
        return f"Detalle {self.id} de Factura {self.factura.num} - {self.cantidad}x {self.producto.descripcion}"

