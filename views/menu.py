"""
Vista - Interfaz de usuario (menús y entrada/salida)
"""

class InterfazMenu:
    """Maneja la interacción con el usuario"""
    
    def __init__(self, gestor):
        self.gestor = gestor
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        print("\n" + "=" * 50)
        print("🏪 PROYECTO FINAL INTEGRADOR PYTHON")
        print("   Sistema de Gestión de Inventario")
        print("=" * 50)
        print("1. 📝 Cargar nuevos productos")
        print("2. 🔍 Consultar productos")
        print("3. ✏️  Modificar productos")
        print("4. 🗑️  Eliminar productos")
        print("5. 🚪 Salir")
        print("=" * 50)
    
    def ejecutar(self):
        """Ejecuta el bucle principal del menú"""
        while True:
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.menu_cargar_producto()
            elif opcion == "2":
                self.menu_consultar()
            elif opcion == "3":
                self.menu_modificar()
            elif opcion == "4":
                self.menu_eliminar()
            elif opcion == "5":
                print("\n👋 Cerrando el sistema. ¡Hasta pronto!")
                break
            else:
                print("❌ Opción inválida. Intente nuevamente.")
    
    def menu_cargar_producto(self):
        """Menú para cargar un nuevo producto"""
        print("\n📝 CARGA DE NUEVOS PRODUCTOS")
        print("-" * 50)
        
        try:
            nombre = input("📦 Nombre del producto: ").strip()
            marca = input("🏷️  Marca: ").strip()
            categoria = input("📂 Categoría: ").strip()
            precio = input("💰 Precio: $").strip()
            stock = input("📊 Stock (cantidad): ").strip()
            descripcion = input("📝 Descripción: ").strip()
            
            self.gestor.agregar_producto(nombre, marca, categoria, precio, stock, descripcion)
            
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def menu_consultar(self):
        """Menú de consultas"""
        print("\n🔍 CONSULTA DE PRODUCTOS")
        print("-" * 50)
        print("1. Ver todos los productos")
        print("2. Ver solo nombres y marcas")
        print("3. Ver precios")
        print("4. Ver stock disponible")
        print("5. Buscar por categoría")
        print("6. Buscar producto por nombre")
        print("7. Volver al menú principal")
        print("-" * 50)
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            self._mostrar_todos_productos()
        elif opcion == "2":
            self._mostrar_nombres_marcas()
        elif opcion == "3":
            self._mostrar_precios()
        elif opcion == "4":
            self._mostrar_stock()
        elif opcion == "5":
            self._buscar_por_categoria()
        elif opcion == "6":
            self._buscar_por_nombre()
        elif opcion == "7":
            print("🔙 Volviendo al menú principal.")
        else:
            print("❌ Opción inválida.")
    
    def _mostrar_todos_productos(self):
        """Muestra todos los productos completos"""
        productos = self.gestor.listar_todos()
        if productos:
            print("\n📋 LISTA COMPLETA DE PRODUCTOS:")
            print("=" * 80)
            for p in productos:
                print(p)
        else:
            print("⚠️ No hay productos en el inventario.")
    
    def _mostrar_nombres_marcas(self):
        """Muestra solo nombres y marcas"""
        datos = self.gestor.obtener_nombres_marcas()
        if datos:
            print("\n🏷️  NOMBRES Y MARCAS DE PRODUCTOS:")
            print("-" * 50)
            for nombre, marca in datos:
                print(f"📦 {nombre} - 🏷️  {marca}")
            print("-" * 50)
        else:
            print("⚠️ No hay productos en el inventario.")
    
    def _mostrar_precios(self):
        """Muestra nombres y precios"""
        datos = self.gestor.obtener_precios()
        if datos:
            print("\n💰 PRECIOS DE PRODUCTOS:")
            print("-" * 50)
            for nombre, precio in datos:
                print(f"📦 {nombre} - 💰 ${precio:.2f}")
            print("-" * 50)
        else:
            print("⚠️ No hay productos en el inventario.")
    
    def _mostrar_stock(self):
        """Muestra nombres y stock"""
        datos = self.gestor.obtener_stock()
        if datos:
            print("\n📊 STOCK DISPONIBLE:")
            print("-" * 50)
            for nombre, stock in datos:
                print(f"📦 {nombre} - 📊 {stock} unidades")
            print("-" * 50)
        else:
            print("⚠️ No hay productos en el inventario.")
    
    def _buscar_por_categoria(self):
        """Busca productos por categoría"""
        categoria = input("\n📂 Ingrese la categoría a buscar: ").strip()
        productos = self.gestor.buscar_por_categoria(categoria)
        
        if productos:
            print(f"\n📋 PRODUCTOS EN LA CATEGORÍA '{categoria.capitalize()}':")
            print("=" * 80)
            for p in productos:
                print(p)
        else:
            print(f"⚠️ No se encontraron productos en la categoría '{categoria}'.")
    
    def _buscar_por_nombre(self):
        """Busca productos por nombre"""
        nombre = input("\n🔍 Ingrese el nombre del producto a buscar: ").strip()
        productos = self.gestor.buscar_por_nombre(nombre)
        
        if productos:
            print(f"\n📋 PRODUCTOS QUE COINCIDEN CON '{nombre}':")
            print("=" * 80)
            for p in productos:
                print(p)
        else:
            print(f"⚠️ No se encontraron productos que coincidan con '{nombre}'.")
    
    def menu_modificar(self):
        """Menú para modificar productos"""
        print("\n✏️  MODIFICAR PRODUCTO")
        print("-" * 50)
        
        try:
            id_producto = int(input("🆔 Ingrese el ID del producto a modificar: "))
        except ValueError:
            print("❌ Error: El ID debe ser un número entero.")
            return
        
        print("\n📋 ¿Qué desea modificar?")
        print("1. Nombre")
        print("2. Marca")
        print("3. Categoría")
        print("4. Precio")
        print("5. Stock")
        print("6. Descripción")
        print("7. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        campos = {
            "1": "nombre",
            "2": "marca",
            "3": "categoria",
            "4": "precio",
            "5": "stock",
            "6": "descripcion"
        }
        
        if opcion not in campos and opcion != "7":
            print("❌ Opción inválida.")
            return
        elif opcion == "7":
            print("🔙 Volviendo al menú principal.")
            return
        
        campo = campos[opcion]
        nuevo_valor = input(f"📝 Ingrese el nuevo valor para {campo}: ").strip()
        
        self.gestor.modificar_producto(id_producto, campo, nuevo_valor)
    
    def menu_eliminar(self):
        """Menú para eliminar productos"""
        print("\n🗑️  ELIMINAR PRODUCTO")
        print("-" * 50)
        
        try:
            id_producto = int(input("🆔 Ingrese el ID del producto a eliminar: "))
            self.gestor.confirmar_eliminacion(id_producto)
        except ValueError:
            print("❌ Error: El ID debe ser un número entero.")