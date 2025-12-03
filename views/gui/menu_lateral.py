"""
Menú Lateral de Navegación
"""
import customtkinter as ctk
from tkinter import messagebox

class MenuLateral:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.crear_menu()
    
    def crear_menu(self):
        """Crea el menú lateral de navegación"""
        self.menu_frame = ctk.CTkFrame(self.parent, width=250, corner_radius=0)
        self.menu_frame.pack(side="left", fill="y", padx=0, pady=0)
        self.menu_frame.pack_propagate(False)
        
        # Título del menú
        titulo = ctk.CTkLabel(
            self.menu_frame, 
            text="📋 MENÚ\nSistema de Inventario",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        titulo.pack(pady=30)
        
        # Botones del menú
        botones = [
            ("🏠 Inicio", "inicio"),
            ("➕ Agregar Producto", "agregar"),
            ("🔍 Consultar Productos", "consultar"),
            ("✏️ Modificar Producto", "modificar"),
            ("🗑️ Eliminar Producto", "eliminar"),
        ]
        
        for texto, accion in botones:
            btn = ctk.CTkButton(
                self.menu_frame,
                text=texto,
                command=lambda a=accion: self.app.mostrar_pantalla(a),
                height=40,
                font=ctk.CTkFont(size=14)
            )
            btn.pack(pady=10, padx=20, fill="x")
        
        # Botón salir en la parte inferior
        btn_salir = ctk.CTkButton(
            self.menu_frame,
            text="🚪 Salir",
            command=self.salir,
            height=40,
            font=ctk.CTkFont(size=14),
            fg_color="red",
            hover_color="darkred"
        )
        btn_salir.pack(side="bottom", pady=20, padx=20, fill="x")
    
    def salir(self):
        """Cierra la aplicación"""
        if messagebox.askokcancel("Salir", "¿Deseas salir del sistema?"):
            self.parent.quit()