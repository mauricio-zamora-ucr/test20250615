# src/mi_app/ui.py

import tkinter as tk
from tkinter import messagebox
from .calculos import Matematicas  # Importamos desde el mismo paquete

class AppUI:
    """Clase que construye la interfaz de usuario con Tkinter."""
    def __init__(self, root):
        self.root = root
        self.root.title("Mi App Genial")
        self.root.geometry("300x150")

        self.label = tk.Label(root, text="¡Haz clic para ver la magia!")
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Calcular 5 + 7", command=self.mostrar_resultado)
        self.button.pack(pady=10)

    def mostrar_resultado(self):
        """Usa la clase de cálculos y muestra el resultado."""
        resultado = Matematicas.sumar(5, 7)
        messagebox.showinfo("Resultado", f"El resultado de la suma es: {resultado}")

    def iniciar(self):
        """Inicia el bucle principal de la aplicación."""
        self.root.mainloop()