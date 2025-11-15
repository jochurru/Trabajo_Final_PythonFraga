# 🎓 Proyecto Final Integrador Python

## Sistema de Gestión de Inventario Eléctrico – Versión POO

Sistema de gestión de inventario desarrollado como **Proyecto Final Integrador** aplicando **Programación Orientada a Objetos (POO)** y el patrón **MVC (Modelo-Vista-Controlador)**.

---

## 🎯 Mejoras de la Versión POO

### ✅ Arquitectura Limpia
- **Separación de responsabilidades** clara entre capas
- **Código reutilizable** y mantenible
- **Escalabilidad** mejorada para futuras funcionalidades

### ✅ Validaciones Robustas
- **Properties** de Python para validación automática
- Manejo de errores mejorado
- Consistencia en el formato de datos

### ✅ Encapsulación
- Lógica de negocio separada de la interfaz
- Acceso a datos centralizado
- Código más testeable

---

## 📦 Estructura del Proyecto

```
Proyecto_Final_Integrador_Python/
├── main.py                          # Punto de entrada
├── models/                          # 🗃️ Capa de Modelos
│   ├── __init__.py
│   ├── producto.py                  # Clase Producto
│   └── database.py                  # Clase InventarioDB
├── controllers/                     # 🎮 Capa de Controladores
│   ├── __init__.py
│   └── gestor_inventario.py        # Clase GestorInventario
└── views/                           # 👁️ Capa de Vistas
    ├── __init__.py
    └── menu.py                      # Clase InterfazMenu
```

---

## 🏗️ Arquitectura del Sistema

### 📐 Patrón MVC Implementado

```
┌─────────────┐
│    VISTA    │  InterfazMenu (menu.py)
│   (View)    │  └─> Interacción con usuario
└──────┬──────┘
       │
       ↓
┌─────────────┐
│ CONTROLADOR │  GestorInventario (gestor_inventario.py)
│(Controller) │  └─> Lógica de negocio
└──────┬──────┘
       │
       ↓
┌─────────────┐
│   MODELO    │  Producto + InventarioDB
│   (Model)   │  └─> Datos y persistencia
└─────────────┘
```

---

## 🧱 Componentes Principales

### 1️⃣ **Producto** (`models/producto.py`)
Representa un producto del inventario con:
- **Validación automática** mediante properties
- Conversión a/desde tuplas de BD
- Representación en string formateada

```python
producto = Producto(
    nombre="Cable Unipolar",
    marca="IMSA",
    categoria="Cables",
    precio=3500.00,
    stock=100,
    descripcion="Cable calibre 4 mm2"
)
```

### 2️⃣ **InventarioDB** (`models/database.py`)
Gestiona toda la interacción con SQLite:
- Conexión y creación de tablas
- Operaciones CRUD completas
- Consultas especializadas
- Manejo de errores robusto

### 3️⃣ **GestorInventario** (`controllers/gestor_inventario.py`)
Coordina la lógica de negocio:
- Validación de datos antes de guardar
- Procesamiento de consultas
- Confirmación de operaciones críticas
- Puente entre vista y modelo

### 4️⃣ **InterfazMenu** (`views/menu.py`)
Maneja toda la interacción con el usuario:
- Menús interactivos
- Captura de entrada
- Formateo de salida
- Navegación del sistema

---

## 🚀 Ejecución

### Instalación
```bash
git clone https://github.com/jochurru/Proyecto_Final_PythonFraga.git
cd Proyecto_Final_Integrador_Python
```

### Ejecutar
```bash
python main.py
```

---

## 📋 Funcionalidades

### ➕ Agregar Productos
- Validación automática de tipos de datos
- Capitalización de nombres
- Verificación de valores negativos

### 🔍 Consultar Productos
- Ver todos los productos
- Filtrar por nombre, categoría
- Vistas especializadas (solo precios, solo stock, etc.)
- Búsqueda parcial de nombres

### ✏️ Modificar Productos
- Modificación campo por campo
- Validación según tipo de dato
- Confirmación de cambios

### 🗑️ Eliminar Productos
- Vista previa del producto
- Confirmación obligatoria
- Verificación de existencia

---

## 🧠 Ventajas de la Versión POO

| Aspecto | Versión Funcional | Versión POO |
|---------|------------------|-------------|
| **Mantenibilidad** | Media | Alta |
| **Reutilización** | Baja | Alta |
| **Testabilidad** | Difícil | Fácil |
| **Escalabilidad** | Limitada | Excelente |
| **Validaciones** | Manuales | Automáticas |
| **Separación de conceptos** | Parcial | Total |

---

## 🔮 Próximas Mejoras Sugeridas

- [ ] **Tests unitarios** con `pytest`
- [ ] **Interfaz gráfica** con Tkinter/PyQt
- [ ] **API REST** con FastAPI/Flask
- [ ] **Exportación** a Excel/CSV
- [ ] **Sistema de usuarios** y permisos
- [ ] **Historial de cambios** (auditoría)
- [ ] **Backup automático** de BD
- [ ] **Reportes** y estadísticas

---

## 🧪 Testing

Para agregar tests unitarios:

```python
# tests/test_producto.py
import pytest
from models.producto import Producto

def test_crear_producto_valido():
    p = Producto("Cable", "Marca", "Cables", 100, 50, "Desc")
    assert p.nombre == "Cable"
    assert p.precio == 100

def test_precio_negativo_falla():
    with pytest.raises(ValueError):
        Producto("Cable", "Marca", "Cables", -100, 50, "Desc")
```

---

## 👨‍💻 Autor

**Jonatan Churruarin**  
Proyecto Final Integrador - Python  

Técnico autodidacta especializado en:
- Desarrollo de sistemas con Python
- Arquitectura de software limpia
- Refactorización y optimización de código
- Implementación de patrones de diseño (MVC, POO)

---

## 📄 Licencia

Este proyecto está disponible como material educativo y de referencia.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

---

## 📧 Contacto

Para consultas o sugerencias sobre este Proyecto Final Integrador.

---

## ⭐ Estado del Proyecto

✅ **Proyecto Final Integrador Completado**  
🎓 **Aplicación práctica de POO y MVC**  
🛠️ **Listo para extensiones**  
📚 **Documentado para uso educativo**  
🎯 **Ejemplo de buenas prácticas en Python**