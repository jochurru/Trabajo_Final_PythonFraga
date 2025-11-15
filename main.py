"""
Proyecto Final Integrador Python - Sistema de Gestión de Inventario
Versión POO (Programación Orientada a Objetos)
Autor: Jonatan Churruarin
"""

from controllers.gestor_inventario import GestorInventario
from views.menu import InterfazMenu

def main():
    """Función principal del sistema"""
    print("\n" + "=" * 60)
    print("🚀 PROYECTO FINAL INTEGRADOR PYTHON")
    print("   Sistema de Gestión de Inventario - POO")
    print("=" * 60)
    
    # Inicializar el gestor de inventario
    gestor = GestorInventario("inventario.db")
    
    # Inicializar la interfaz de usuario
    interfaz = InterfazMenu(gestor)
    
    # Ejecutar el menú principal
    interfaz.ejecutar()

if __name__ == "__main__":
    main()