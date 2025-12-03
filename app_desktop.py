"""
Proyecto Final Integrador Python - Versión Desktop
App de Escritorio con CustomTkinter (Modularizada)
Autor: Jonatan Churruarin
"""

import customtkinter as ctk
from controllers.gestor_inventario import GestorInventario
from views.gui.pantalla_inicio import PantallaInicio
from views.gui.pantalla_agregar import PantallaAgregar
from views.gui.pantalla_consultar import PantallaConsultar
from views.gui.pantalla_modificar import PantallaModificar
from views.gui.pantalla_eliminar import PantallaEliminar
from views.gui.menu_lateral import MenuLateral

# Configuración de tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class InventarioApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal
        self.title("🔌 Proyecto Final Integrador Python")
        self.geometry("1200x700")
        self.resizable(True, True)
        
        # Inicializar gestor
        self.gestor = GestorInventario("inventario.db")
        
        # Crear contenedor principal
        self.contenido_frame = ctk.CTkFrame(self, corner_radius=0)
        self.contenido_frame.pack(side="right", fill="both", expand=True)
        
        # Crear menú lateral
        self.menu = MenuLateral(self, self)
        
        # Inicializar pantallas
        self.pantalla_inicio = PantallaInicio(self.contenido_frame, self.gestor)
        self.pantalla_agregar = PantallaAgregar(self.contenido_frame, self.gestor)
        self.pantalla_consultar = PantallaConsultar(self.contenido_frame, self.gestor)
        self.pantalla_modificar = PantallaModificar(self.contenido_frame, self.gestor)
        self.pantalla_eliminar = PantallaEliminar(self.contenido_frame, self.gestor)
        
        # Mostrar inicio por defecto
        self.mostrar_pantalla("inicio")
    
    def limpiar_contenido(self):
        """Limpia el contenido actual"""
        for widget in self.contenido_frame.winfo_children():
            widget.pack_forget()
    
    def mostrar_pantalla(self, nombre):
        """Muestra la pantalla solicitada"""
        self.limpiar_contenido()
        
        if nombre == "inicio":
            self.pantalla_inicio.mostrar()
        elif nombre == "agregar":
            self.pantalla_agregar.mostrar()
        elif nombre == "consultar":
            self.pantalla_consultar.mostrar()
        elif nombre == "modificar":
            self.pantalla_modificar.mostrar()
        elif nombre == "eliminar":
            self.pantalla_eliminar.mostrar()

def main():
    app = InventarioApp()
    app.mainloop()

if __name__ == "__main__":
    main()