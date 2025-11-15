"""
Modelo de datos para Producto
"""

class Producto:
    """Representa un producto del inventario"""
    
    def __init__(self, nombre, marca, categoria, precio, stock, descripcion, id_producto=None):
        self.id = id_producto
        self.nombre = nombre
        self.marca = marca
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip().capitalize()
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, valor):
        self._marca = valor.strip().capitalize() if valor else ""
    
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor):
        self._categoria = valor.strip().capitalize() if valor else ""
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        try:
            precio_float = float(valor)
            if precio_float < 0:
                raise ValueError("El precio no puede ser negativo")
            self._precio = precio_float
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser un número válido")
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, valor):
        try:
            stock_int = int(valor)
            if stock_int < 0:
                raise ValueError("El stock no puede ser negativo")
            self._stock = stock_int
        except (ValueError, TypeError):
            raise ValueError("El stock debe ser un número entero válido")
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor.strip().capitalize() if valor else ""
    
    def __str__(self):
        return f"""
🆔 ID: {self.id}
📦 Nombre: {self.nombre}
🏷️ Marca: {self.marca}
📂 Categoría: {self.categoria}
💰 Precio: ${self.precio:.2f}
📦 Stock: {self.stock} unidades
📝 Descripción: {self.descripcion}
{'-' * 80}"""
    
    def to_dict(self):
        """Convierte el producto a diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'marca': self.marca,
            'categoria': self.categoria,
            'precio': self.precio,
            'stock': self.stock,
            'descripcion': self.descripcion
        }
    
    @classmethod
    def from_tuple(cls, tupla):
        """Crea un producto desde una tupla de la base de datos"""
        return cls(
            id_producto=tupla[0],
            nombre=tupla[1],
            marca=tupla[2],
            categoria=tupla[3],
            precio=tupla[4],
            stock=tupla[5],
            descripcion=tupla[6]
        )