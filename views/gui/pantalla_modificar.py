"""
Pantalla para Modificar Productos
"""
import customtkinter as ctk
from tkinter import messagebox

class PantallaModificar:
    def __init__(self, parent, gestor):
        self.parent = parent
        self.gestor = gestor
        self.frame = ctk.CTkFrame(parent)
        self.producto_modificar_id = None
    
    def mostrar(self):
        """Muestra la pantalla de modificar productos"""
        self.frame.pack(fill="both", expand=True)
        
        # Limpiar contenido previo
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        titulo = ctk.CTkLabel(
            self.frame,
            text="✏️ Modificar Producto",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        titulo.pack(pady=30)
        
        # Frame de búsqueda
        self.crear_frame_busqueda()
        
        # Frame para resultados de búsqueda
        self.resultados_frame = ctk.CTkScrollableFrame(self.frame, height=150)
        self.resultados_frame.pack(pady=10, padx=50, fill="both")
        
        # Frame del formulario
        self.form_frame = ctk.CTkFrame(self.frame)
        self.form_frame.pack(pady=20, padx=50, fill="both", expand=True)
        
        # Mensaje inicial
        msg = ctk.CTkLabel(
            self.form_frame, 
            text="👆 Busca y selecciona un producto para modificar", 
            font=ctk.CTkFont(size=14)
        )
        msg.pack(pady=50)
    
    def crear_frame_busqueda(self):
        """Crea el frame de búsqueda"""
        busqueda_frame = ctk.CTkFrame(self.frame)
        busqueda_frame.pack(pady=20, padx=50, fill="x")
        
        ctk.CTkLabel(
            busqueda_frame, 
            text="Buscar producto:", 
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=10)
        
        # Opciones de búsqueda
        opciones_frame = ctk.CTkFrame(busqueda_frame)
        opciones_frame.pack(pady=10, fill="x", padx=20)
        
        ctk.CTkLabel(opciones_frame, text="Buscar por:").pack(side="left", padx=10)
        
        self.tipo_busqueda = ctk.CTkSegmentedButton(
            opciones_frame,
            values=["ID", "Nombre", "Marca", "Categoría"],
            command=self.cambiar_tipo_busqueda
        )
        self.tipo_busqueda.pack(side="left", padx=10)
        self.tipo_busqueda.set("Nombre")
        
        # Campo de búsqueda
        buscar_frame = ctk.CTkFrame(busqueda_frame)
        buscar_frame.pack(pady=10, fill="x", padx=20)
        
        self.entry_buscar = ctk.CTkEntry(
            buscar_frame, 
            width=400, 
            height=35, 
            placeholder_text="Escribe para buscar..."
        )
        self.entry_buscar.pack(side="left", padx=10)
        
        ctk.CTkButton(
            buscar_frame, 
            text="🔍 Buscar", 
            command=self.buscar_productos,
            width=100, 
            height=35
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            buscar_frame, 
            text="🔄 Limpiar", 
            command=self.limpiar_busqueda,
            width=100, 
            height=35, 
            fg_color="gray"
        ).pack(side="left", padx=5)
    
    def cambiar_tipo_busqueda(self, valor):
        """Cambia el placeholder según el tipo de búsqueda"""
        placeholders = {
            "ID": "Ingresa el ID del producto...",
            "Nombre": "Ingresa el nombre del producto...",
            "Marca": "Ingresa la marca...",
            "Categoría": "Ingresa la categoría..."
        }
        self.entry_buscar.configure(
            placeholder_text=placeholders.get(valor, "Escribe para buscar...")
        )
        self.entry_buscar.delete(0, "end")
    
    def limpiar_busqueda(self):
        """Limpia la búsqueda y resultados"""
        self.entry_buscar.delete(0, "end")
        
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()
        
        for widget in self.form_frame.winfo_children():
            widget.destroy()
        
        msg = ctk.CTkLabel(
            self.form_frame,
            text="👆 Busca y selecciona un producto para modificar",
            font=ctk.CTkFont(size=14)
        )
        msg.pack(pady=50)
    
    def buscar_productos(self):
        """Busca productos según el criterio seleccionado"""
        tipo = self.tipo_busqueda.get()
        termino = self.entry_buscar.get().strip()
        
        if not termino:
            messagebox.showwarning("Advertencia", "Ingresa un término de búsqueda")
            return
        
        # Limpiar resultados previos
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()
        
        # Buscar según tipo
        productos = self.obtener_productos(tipo, termino)
        
        # Mostrar resultados
        self.mostrar_resultados(productos)
    
    def obtener_productos(self, tipo, termino):
        """Obtiene productos según el tipo de búsqueda"""
        try:
            if tipo == "ID":
                producto = self.gestor.buscar_producto_por_id(int(termino))
                return [producto] if producto else []
            elif tipo == "Nombre":
                return self.gestor.buscar_por_nombre(termino)
            elif tipo == "Marca":
                todos = self.gestor.listar_todos()
                return [p for p in todos if termino.lower() in p.marca.lower()]
            elif tipo == "Categoría":
                return self.gestor.buscar_por_categoria(termino)
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número")
            return []
    
    def mostrar_resultados(self, productos):
        """Muestra los resultados de la búsqueda"""
        if not productos:
            ctk.CTkLabel(
                self.resultados_frame,
                text="❌ No se encontraron productos",
                font=ctk.CTkFont(size=14)
            ).pack(pady=20)
            return
        
        ctk.CTkLabel(
            self.resultados_frame,
            text=f"✅ Se encontraron {len(productos)} producto(s):",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=10)
        
        for producto in productos:
            self.crear_item_resultado(producto)
    
    def crear_item_resultado(self, producto):
        """Crea un item de resultado"""
        resultado_frame = ctk.CTkFrame(self.resultados_frame)
        resultado_frame.pack(pady=5, padx=10, fill="x")
        
        info_text = (
            f"ID: {producto.id} | {producto.nombre} | {producto.marca} | "
            f"{producto.categoria} | ${producto.precio:.2f} | Stock: {producto.stock}"
        )
        
        ctk.CTkLabel(
            resultado_frame,
            text=info_text,
            font=ctk.CTkFont(size=12)
        ).pack(side="left", padx=10, pady=10)
        
        ctk.CTkButton(
            resultado_frame,
            text="✏️ Seleccionar",
            command=lambda p=producto: self.cargar_producto(p),
            width=120,
            height=30
        ).pack(side="right", padx=10)
    
    def cargar_producto(self, producto):
        """Carga los datos del producto en el formulario"""
        # Limpiar frame
        for widget in self.form_frame.winfo_children():
            widget.destroy()
        
        # Título
        ctk.CTkLabel(
            self.form_frame,
            text=f"Modificando: {producto.nombre}",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(pady=10)
        
        # Frame con scroll
        scrollable = ctk.CTkScrollableFrame(self.form_frame, width=500, height=350)
        scrollable.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Crear campos del formulario
        self.crear_formulario(scrollable, producto)
        
        # Guardar ID del producto
        self.producto_modificar_id = producto.id
    
    def crear_formulario(self, parent, producto):
        """Crea el formulario de modificación"""
        campos = [
            ("Nombre del Producto *", "entry_mod_nombre", producto.nombre),
            ("Marca", "entry_mod_marca", producto.marca),
            ("Categoría", "entry_mod_categoria", producto.categoria),
            ("Precio *", "entry_mod_precio", str(producto.precio)),
            ("Stock *", "entry_mod_stock", str(producto.stock)),
        ]
        
        for label, attr, valor in campos:
            ctk.CTkLabel(parent, text=label, font=ctk.CTkFont(size=14)).pack(pady=5)
            entry = ctk.CTkEntry(parent, width=400, height=35)
            entry.pack(pady=5)
            entry.insert(0, valor)
            setattr(self, attr, entry)
        
        # Campo descripción
        ctk.CTkLabel(parent, text="Descripción", font=ctk.CTkFont(size=14)).pack(pady=5)
        self.entry_mod_descripcion = ctk.CTkTextbox(parent, width=400, height=80)
        self.entry_mod_descripcion.pack(pady=5)
        self.entry_mod_descripcion.insert("1.0", producto.descripcion)
        
        # Botón guardar
        ctk.CTkButton(
            parent,
            text="💾 GUARDAR CAMBIOS",
            command=self.guardar_modificacion,
            height=50,
            width=400,
            font=ctk.CTkFont(size=18, weight="bold"),
            fg_color="green",
            hover_color="darkgreen"
        ).pack(pady=30)
    
    def guardar_modificacion(self):
        """Guarda las modificaciones del producto"""
        nombre = self.entry_mod_nombre.get()
        marca = self.entry_mod_marca.get()
        categoria = self.entry_mod_categoria.get()
        precio = self.entry_mod_precio.get()
        stock = self.entry_mod_stock.get()
        descripcion = self.entry_mod_descripcion.get("1.0", "end-1c")
        
        if not nombre or not precio or not stock:
            messagebox.showerror("Error", "Completa los campos obligatorios (*)")
            return
        
        try:
            # Actualizar todos los campos
            campos = [
                ("nombre", nombre),
                ("marca", marca),
                ("categoria", categoria),
                ("precio", precio),
                ("stock", stock),
                ("descripcion", descripcion)
            ]
            
            for campo, valor in campos:
                self.gestor.modificar_producto(self.producto_modificar_id, campo, valor)
            
            messagebox.showinfo("Éxito", "Producto modificado correctamente")
            self.mostrar()  # Recargar pantalla
        except Exception as e:
            messagebox.showerror("Error", str(e))