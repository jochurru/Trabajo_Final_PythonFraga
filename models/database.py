"""
Capa de acceso a datos - Gestión de base de datos SQLite
"""
import sqlite3
from models.producto import Producto

class InventarioDB:
    """Maneja todas las operaciones con la base de datos"""
    
    def __init__(self, nombre_bd="inventario.db"):
        self.nombre_bd = nombre_bd
        self._crear_tabla()
    
    def _conectar(self):
        """Establece conexión con la base de datos"""
        try:
            conn = sqlite3.connect(self.nombre_bd)
            return conn
        except sqlite3.Error as e:
            print(f"❌ Error al conectar a la base de datos: {e}")
            return None
    
    def _crear_tabla(self):
        """Crea la tabla productos si no existe"""
        conn = self._conectar()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS productos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        marca TEXT,
                        categoria TEXT,
                        precio REAL NOT NULL,
                        stock INTEGER NOT NULL,
                        descripcion TEXT
                    )
                ''')
                conn.commit()
                print("✅ Tabla 'productos' verificada/creada correctamente.")
            except sqlite3.Error as e:
                print(f"❌ Error al crear la tabla: {e}")
            finally:
                conn.close()
    
    def insertar_producto(self, producto):
        """Inserta un nuevo producto en la base de datos"""
        conn = self._conectar()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO productos (nombre, marca, categoria, precio, stock, descripcion)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (producto.nombre, producto.marca, producto.categoria, 
                producto.precio, producto.stock, producto.descripcion))
            conn.commit()
            producto.id = cursor.lastrowid
            print(f"✅ Producto '{producto.nombre}' insertado correctamente con ID {producto.id}.")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error al insertar producto: {e}")
            return False
        finally:
            conn.close()
    
    def obtener_todos(self):
        """Obtiene todos los productos"""
        conn = self._conectar()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos")
            resultados = cursor.fetchall()
            return [Producto.from_tuple(r) for r in resultados]
        except sqlite3.Error as e:
            print(f"❌ Error al obtener productos: {e}")
            return []
        finally:
            conn.close()
    
    def obtener_por_id(self, id_producto):
        """Obtiene un producto por su ID"""
        conn = self._conectar()
        if not conn:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
            resultado = cursor.fetchone()
            return Producto.from_tuple(resultado) if resultado else None
        except sqlite3.Error as e:
            print(f"❌ Error al obtener producto: {e}")
            return None
        finally:
            conn.close()
    
    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre (búsqueda parcial)"""
        conn = self._conectar()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))
            resultados = cursor.fetchall()
            return [Producto.from_tuple(r) for r in resultados]
        except sqlite3.Error as e:
            print(f"❌ Error al buscar productos: {e}")
            return []
        finally:
            conn.close()
    
    def buscar_por_categoria(self, categoria):
        """Busca productos por categoría"""
        conn = self._conectar()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos WHERE categoria = ?", (categoria,))
            resultados = cursor.fetchall()
            return [Producto.from_tuple(r) for r in resultados]
        except sqlite3.Error as e:
            print(f"❌ Error al buscar por categoría: {e}")
            return []
        finally:
            conn.close()
    
    def obtener_nombres_marcas(self):
        """Obtiene solo nombres y marcas"""
        conn = self._conectar()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, marca FROM productos")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Error al obtener nombres y marcas: {e}")
            return []
        finally:
            conn.close()
    
    def obtener_precios(self):
        """Obtiene nombres y precios"""
        conn = self._conectar()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, precio FROM productos")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Error al obtener precios: {e}")
            return []
        finally:
            conn.close()
    
    def obtener_stock(self):
        """Obtiene nombres y stock"""
        conn = self._conectar()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, stock FROM productos")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Error al obtener stock: {e}")
            return []
        finally:
            conn.close()
    
    def actualizar_producto(self, id_producto, campo, nuevo_valor):
        """Actualiza un campo específico de un producto"""
        conn = self._conectar()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            query = f"UPDATE productos SET {campo} = ? WHERE id = ?"
            cursor.execute(query, (nuevo_valor, id_producto))
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"✅ Producto ID {id_producto} modificado correctamente.")
                return True
            else:
                print(f"⚠️ No se encontró el producto con ID {id_producto}.")
                return False
        except sqlite3.Error as e:
            print(f"❌ Error al actualizar producto: {e}")
            return False
        finally:
            conn.close()
    
    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID"""
        conn = self._conectar()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"✅ Producto ID {id_producto} eliminado correctamente.")
                return True
            else:
                print(f"⚠️ No se encontró el producto con ID {id_producto}.")
                return False
        except sqlite3.Error as e:
            print(f"❌ Error al eliminar producto: {e}")
            return False
        finally:
            conn.close()