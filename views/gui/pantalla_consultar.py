"""
Pantalla para Consultar Productos
"""
import customtkinter as ctk
from tkinter import ttk

class PantallaConsultar:
    def __init__(self, parent, gestor):
        self.parent = parent
        self.gestor = gestor
        self.frame = ctk.CTkFrame(parent)
    
    def mostrar(self):
        """Muestra la pantalla de consultar productos"""
        self.frame.pack(fill="both", expand=True)
        
        # Limpiar contenido previo
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        titulo = ctk.CTkLabel(
            self.frame,
            text="🔍 Consultar Productos",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        titulo.pack(pady=20)
        
        # Frame de búsqueda
        busqueda_frame = ctk.CTkFrame(self.frame)
        busqueda_frame.pack(pady=10, padx=50, fill="x")
        
        ctk.CTkLabel(busqueda_frame, text="Buscar por nombre:", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
        self.entry_buscar = ctk.CTkEntry(busqueda_frame, width=300)
        self.entry_buscar.pack(side="left", padx=10)
        
        btn_buscar = ctk.CTkButton(busqueda_frame, text="🔍 Buscar", command=self.buscar_productos)
        btn_buscar.pack(side="left", padx=10)
        
        btn_todos = ctk.CTkButton(busqueda_frame, text="📋 Ver Todos", command=self.mostrar_todos_productos)
        btn_todos.pack(side="left", padx=10)
        
        # Frame para la tabla
        self.tabla_frame = ctk.CTkFrame(self.frame)
        self.tabla_frame.pack(pady=10, padx=50, fill="both", expand=True)
        
        self.mostrar_todos_productos()
    
    def mostrar_todos_productos(self):
        """Muestra todos los productos en la tabla"""
        for widget in self.tabla_frame.winfo_children():
            widget.destroy()
        
        productos = self.gestor.listar_todos()
        self.crear_tabla(productos)
    
    def buscar_productos(self):
        """Busca productos por nombre"""
        for widget in self.tabla_frame.winfo_children():
            widget.destroy()
        
        nombre = self.entry_buscar.get()
        if nombre:
            productos = self.gestor.buscar_por_nombre(nombre)
        else:
            productos = self.gestor.listar_todos()
        
        self.crear_tabla(productos)
    
    def crear_tabla(self, productos):
        """Crea una tabla con los productos"""
        if not productos:
            label = ctk.CTkLabel(self.tabla_frame, text="No se encontraron productos", font=ctk.CTkFont(size=16))
            label.pack(pady=20)
            return
        
        # Configurar estilo
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b")
        style.configure("Treeview.Heading", background="#1f538d", foreground="white")
        
        # Crear tabla
        tabla = ttk.Treeview(
            self.tabla_frame, 
            columns=("ID", "Nombre", "Marca", "Categoría", "Precio", "Stock"), 
            show="headings"
        )
        
        # Configurar columnas
        columnas = [
            ("ID", 50),
            ("Nombre", 200),
            ("Marca", 150),
            ("Categoría", 150),
            ("Precio", 100),
            ("Stock", 100)
        ]
        
        for col, ancho in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=ancho)
        
        # Insertar datos
        for p in productos:
            tabla.insert("", "end", values=(
                p.id, p.nombre, p.marca, p.categoria, 
                f"${p.precio:.2f}", p.stock
            ))
        
        tabla.pack(fill="both", expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tabla_frame, orient="vertical", command=tabla.yview)
        scrollbar.pack(side="right", fill="y")
        tabla.configure(yscrollcommand=scrollbar.set)