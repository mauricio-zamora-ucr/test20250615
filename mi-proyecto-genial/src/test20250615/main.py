# src/mi_app/main.py

import tkinter as tk
from .ui import AppUI

def iniciar_app():
    """
    Punto de entrada principal.
    Crea la ventana raíz y la instancia de la UI.
    """
    print("🚀 Iniciando la aplicación...")
    try:
        root = tk.Tk()
        app = AppUI(root)
        app.iniciar()
    except tk.TclError as e:
        print(f"No se pudo iniciar la interfaz gráfica. ¿Estás en un entorno sin pantalla? Error: {e}")
        print("La aplicación funcionaría en un entorno de escritorio.")

if __name__ == '__main__':
    iniciar_app()