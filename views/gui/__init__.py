"""
Paquete de vistas GUI (Interfaz Gráfica)
"""
from .menu_lateral import MenuLateral
from .pantalla_inicio import PantallaInicio
from .pantalla_agregar import PantallaAgregar
from .pantalla_consultar import PantallaConsultar
from .pantalla_modificar import PantallaModificar
from .pantalla_eliminar import PantallaEliminar

__all__ = [
    'MenuLateral',
    'PantallaInicio',
    'PantallaAgregar',
    'PantallaConsultar',
    'PantallaModificar',
    'PantallaEliminar'
]