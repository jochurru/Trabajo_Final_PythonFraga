"""
Pantalla de Inicio - Dashboard
"""
import customtkinter as ctk

class PantallaInicio:
    def __init__(self, parent, gestor):
        self.parent = parent
        self.gestor = gestor
        self.frame = ctk.CTkFrame(parent)
    
    def mostrar(self):
        """Muestra la pantalla de inicio"""
        self.frame.pack(fill="both", expand=True)
        
        # Limpiar contenido previo
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        # Título
        titulo = ctk.CTkLabel(
            self.frame,
            text="🔌 Proyecto Final Integrador Python",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        titulo.pack(pady=30)
        
        subtitulo = ctk.CTkLabel(
            self.frame,
            text="Sistema de Gestión de Inventario Eléctrico - POO",
            font=ctk.CTkFont(size=16)
        )
        subtitulo.pack(pady=10)
        
        # Frame de métricas
        metricas_frame = ctk.CTkFrame(self.frame)
        metricas_frame.pack(pady=30, padx=50, fill="x")
        
        productos = self.gestor.listar_todos()
        total_productos = len(productos)
        stock_total = sum([p.stock for p in productos])
        valor_total = sum([p.precio * p.stock for p in productos])
        
        # Métricas
        metricas = [
            ("📦 Total Productos", str(total_productos)),
            ("📊 Stock Total", f"{stock_total} unidades"),
            ("💰 Valor Inventario", f"${valor_total:,.2f}")
        ]
        
        for titulo_metrica, valor in metricas:
            m = ctk.CTkFrame(metricas_frame)
            m.pack(side="left", expand=True, padx=20, pady=20)
            ctk.CTkLabel(m, text=titulo_metrica, font=ctk.CTkFont(size=16)).pack(pady=10)
            ctk.CTkLabel(m, text=valor, font=ctk.CTkFont(size=32, weight="bold")).pack(pady=10)
        
        # Información adicional
        info = ctk.CTkLabel(
            self.frame,
            text="Usa el menú lateral para gestionar tu inventario",
            font=ctk.CTkFont(size=14)
        )
        info.pack(pady=20)