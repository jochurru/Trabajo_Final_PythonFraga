"""
Pantalla para Agregar Productos
"""
import customtkinter as ctk
from tkinter import messagebox

class PantallaAgregar:
    def __init__(self, parent, gestor):
        self.parent = parent
        self.gestor = gestor
        self.frame = ctk.CTkFrame(parent)
    
    def mostrar(self):
        """Muestra la pantalla de agregar productos"""
        self.frame.pack(fill="both", expand=True)
        
        # Limpiar contenido previo
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        titulo = ctk.CTkLabel(
            self.frame,
            text="➕ Agregar Nuevo Producto",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        titulo.pack(pady=30)
        
        # Frame del formulario
        form_frame = ctk.CTkFrame(self.frame)
        form_frame.pack(pady=20, padx=100, fill="both", expand=True)
        
        # Campos del formulario
        campos = [
            ("Nombre del Producto *", "entry_nombre"),
            ("Marca", "entry_marca"),
            ("Categoría", "entry_categoria"),
            ("Precio *", "entry_precio"),
            ("Stock *", "entry_stock"),
        ]
        
        for label, attr in campos:
            ctk.CTkLabel(form_frame, text=label, font=ctk.CTkFont(size=14)).pack(pady=5)
            entry = ctk.CTkEntry(form_frame, width=400, height=35)
            entry.pack(pady=5)
            setattr(self, attr, entry)
        
        # Campo descripción (textbox)
        ctk.CTkLabel(form_frame, text="Descripción", font=ctk.CTkFont(size=14)).pack(pady=5)
        self.entry_descripcion = ctk.CTkTextbox(form_frame, width=400, height=80)
        self.entry_descripcion.pack(pady=5)
        
        # Botón guardar
        btn_guardar = ctk.CTkButton(
            form_frame,
            text="✅ Guardar Producto",
            command=self.guardar_producto,
            height=40,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        btn_guardar.pack(pady=20)
    
    def guardar_producto(self):
        """Guarda el producto en la base de datos"""
        nombre = self.entry_nombre.get()
        marca = self.entry_marca.get()
        categoria = self.entry_categoria.get()
        precio = self.entry_precio.get()
        stock = self.entry_stock.get()
        descripcion = self.entry_descripcion.get("1.0", "end-1c")
        
        if not nombre or not precio or not stock:
            messagebox.showerror("Error", "Completa los campos obligatorios (*)")
            return
        
        try:
            success = self.gestor.agregar_producto(nombre, marca, categoria, precio, stock, descripcion)
            if success:
                messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente")
                self.mostrar()  # Limpiar formulario
            else:
                messagebox.showerror("Error", "No se pudo agregar el producto")
        except Exception as e:
            messagebox.showerror("Error", str(e))