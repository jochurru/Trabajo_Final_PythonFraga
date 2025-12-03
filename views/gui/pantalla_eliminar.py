"""
Pantalla para Eliminar Productos
"""
import customtkinter as ctk
from tkinter import messagebox

class PantallaEliminar:
    def __init__(self, parent, gestor):
        self.parent = parent
        self.gestor = gestor
        self.frame = ctk.CTkFrame(parent)
        self.producto_eliminar_id = None
        self.check_confirmar = None
    
    def mostrar(self):
        """Muestra la pantalla de eliminar productos"""
        self.frame.pack(fill="both", expand=True)
        
        # Limpiar contenido previo
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        titulo = ctk.CTkLabel(
            self.frame,
            text="🗑️ Eliminar Producto",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        titulo.pack(pady=30)
        
        # Frame de búsqueda
        self.crear_frame_busqueda()
        
        # Frame para resultados de búsqueda
        self.resultados_frame = ctk.CTkScrollableFrame(self.frame, height=150)
        self.resultados_frame.pack(pady=10, padx=50, fill="both")
        
        # Frame para detalles del producto
        self.detalles_frame = ctk.CTkFrame(self.frame)
        self.detalles_frame.pack(pady=20, padx=50, fill="both", expand=True)
        
        # Mensaje inicial
        msg = ctk.CTkLabel(
            self.detalles_frame,
            text="👆 Busca y selecciona un producto para eliminar",
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
        
        for widget in self.detalles_frame.winfo_children():
            widget.destroy()
        
        msg = ctk.CTkLabel(
            self.detalles_frame,
            text="👆 Busca y selecciona un producto para eliminar",
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
        
        for widget in self.detalles_frame.winfo_children():
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
            
            msg = ctk.CTkLabel(
                self.detalles_frame,
                text="👆 Busca y selecciona un producto para eliminar",
                font=ctk.CTkFont(size=14)
            )
            msg.pack(pady=50)
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
            text="🗑️ Seleccionar",
            command=lambda p=producto: self.ver_producto(p),
            width=120,
            height=30,
            fg_color="red",
            hover_color="darkred"
        ).pack(side="right", padx=10)
    
    def ver_producto(self, producto):
        """Muestra los detalles del producto a eliminar"""
        # Limpiar frame
        for widget in self.detalles_frame.winfo_children():
            widget.destroy()
        
        # Crear scrollable frame para que todo sea visible
        scrollable = ctk.CTkScrollableFrame(self.detalles_frame, width=600, height=400)
        scrollable.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Advertencia
        ctk.CTkLabel(
            scrollable,
            text="⚠️ ADVERTENCIA: Esta acción no se puede deshacer",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="red"
        ).pack(pady=20)
        
        # Frame de información
        info_frame = ctk.CTkFrame(scrollable)
        info_frame.pack(pady=20, padx=20, fill="x")
        
        # Detalles del producto
        detalles = [
            ("🆔 ID", producto.id),
            ("📦 Nombre", producto.nombre),
            ("🏷️ Marca", producto.marca),
            ("📂 Categoría", producto.categoria),
            ("💰 Precio", f"${producto.precio:.2f}"),
            ("📊 Stock", f"{producto.stock} unidades"),
            ("📝 Descripción", producto.descripcion)
        ]
        
        for label, valor in detalles:
            detalle_frame = ctk.CTkFrame(info_frame)
            detalle_frame.pack(pady=5, padx=10, fill="x")
            
            ctk.CTkLabel(
                detalle_frame,
                text=f"{label}:",
                font=ctk.CTkFont(size=14, weight="bold"),
                width=150,
                anchor="w"
            ).pack(side="left", padx=5)
            
            ctk.CTkLabel(
                detalle_frame,
                text=str(valor),
                font=ctk.CTkFont(size=14),
                anchor="w"
            ).pack(side="left", padx=5)
        
        # Separador
        ctk.CTkLabel(scrollable, text="─" * 50).pack(pady=20)
        
        # Guardar el ID
        self.producto_eliminar_id = producto.id
        
        # Checkbox de confirmación (MÁS GRANDE)
        self.check_confirmar = ctk.CTkCheckBox(
            scrollable,
            text="✅ Confirmo que deseo eliminar este producto",
            font=ctk.CTkFont(size=16, weight="bold"),
            checkbox_width=30,
            checkbox_height=30
        )
        self.check_confirmar.pack(pady=30)
        
        # Botón eliminar (MÁS GRANDE Y VISIBLE)
        btn_eliminar = ctk.CTkButton(
            scrollable,
            text="🗑️ ELIMINAR PRODUCTO",
            command=self.confirmar_eliminacion,
            height=60,
            width=400,
            font=ctk.CTkFont(size=20, weight="bold"),
            fg_color="red",
            hover_color="darkred"
        )
        btn_eliminar.pack(pady=30)
    
    def confirmar_eliminacion(self):
        """Confirma y elimina el producto"""
        if not self.check_confirmar.get():
            messagebox.showwarning("Advertencia", "Debes confirmar la eliminación")
            return
        
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este producto?"):
            try:
                success = self.gestor.eliminar_producto(self.producto_eliminar_id)
                if success:
                    messagebox.showinfo("Éxito", "Producto eliminado correctamente")
                    self.mostrar()  # Recargar pantalla
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el producto")
            except Exception as e:
                messagebox.showerror("Error", str(e))