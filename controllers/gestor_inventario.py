"""
Controlador - Lógica de negocio del inventario
"""
from models.database import InventarioDB
from models.producto import Producto

class GestorInventario:
    """Coordina las operaciones del inventario"""
    
    def __init__(self, nombre_bd="inventario.db"):
        self.db = InventarioDB(nombre_bd)
    
    def agregar_producto(self, nombre, marca, categoria, precio, stock, descripcion):
        """Agrega un nuevo producto al inventario"""
        try:
            producto = Producto(nombre, marca, categoria, precio, stock, descripcion)
            return self.db.insertar_producto(producto)
        except ValueError as e:
            print(f"❌ Error de validación: {e}")
            return False
    
    def listar_todos(self):
        """Obtiene todos los productos"""
        return self.db.obtener_todos()
    
    def buscar_producto_por_id(self, id_producto):
        """Busca un producto específico por ID"""
        return self.db.obtener_por_id(id_producto)
    
    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre"""
        return self.db.buscar_por_nombre(nombre)
    
    def buscar_por_categoria(self, categoria):
        """Busca productos por categoría"""
        return self.db.buscar_por_categoria(categoria.strip().capitalize())
    
    def obtener_nombres_marcas(self):
        """Obtiene listado de nombres y marcas"""
        return self.db.obtener_nombres_marcas()
    
    def obtener_precios(self):
        """Obtiene listado de precios"""
        return self.db.obtener_precios()
    
    def obtener_stock(self):
        """Obtiene listado de stock"""
        return self.db.obtener_stock()
    
    def modificar_producto(self, id_producto, campo, nuevo_valor):
        """Modifica un campo específico de un producto"""
        # Validar que el producto existe
        producto = self.db.obtener_por_id(id_producto)
        if not producto:
            print(f"⚠️ No se encontró el producto con ID {id_producto}.")
            return False
        
        # Validar el nuevo valor según el campo
        try:
            if campo == "precio":
                nuevo_valor = float(nuevo_valor)
                if nuevo_valor < 0:
                    raise ValueError("El precio no puede ser negativo")
            elif campo == "stock":
                nuevo_valor = int(nuevo_valor)
                if nuevo_valor < 0:
                    raise ValueError("El stock no puede ser negativo")
            elif campo in ["nombre", "marca", "categoria", "descripcion"]:
                nuevo_valor = nuevo_valor.strip().capitalize()
                if campo == "nombre" and not nuevo_valor:
                    raise ValueError("El nombre no puede estar vacío")
        except ValueError as e:
            print(f"❌ Error de validación: {e}")
            return False
        
        return self.db.actualizar_producto(id_producto, campo, nuevo_valor)
    
    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario"""
        # Verificar que existe antes de eliminar
        producto = self.db.obtener_por_id(id_producto)
        if not producto:
            print(f"⚠️ No se encontró el producto con ID {id_producto}.")
            return False
        
        return self.db.eliminar_producto(id_producto)
    
    def confirmar_eliminacion(self, id_producto):
        """Muestra el producto y solicita confirmación antes de eliminar"""
        producto = self.db.obtener_por_id(id_producto)
        if not producto:
            return False
        
        print(f"\n🧾 Producto encontrado:")
        print(f"ID: {producto.id} | Nombre: {producto.nombre} | Marca: {producto.marca}")
        print(f"Categoría: {producto.categoria} | Precio: ${producto.precio:.2f} | Stock: {producto.stock}")
        
        confirmacion = input("\n❗ ¿Está seguro que desea eliminar este producto? (s/n): ").strip().lower()
        
        if confirmacion == "s":
            return self.eliminar_producto(id_producto)
        else:
            print("↩ Eliminación cancelada.")
            return False