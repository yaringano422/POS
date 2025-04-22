# ui/forms.py
import tkinter as tk
from tkinter import ttk

class Form:
    def __init__(self, parent, fields):
        """
        Constructor para un formulario reutilizable.
        
        Args:
            parent (tk.Widget): El widget padre del formulario.
            fields (list): Lista de nombres de campos para crear entradas.
        """
        self.parent = parent
        self.fields = fields
        self.entries = {}

        self.create_form()

    def create_form(self):
        for field in self.fields:
            frame = tk.Frame(self.parent)
            frame.pack(fill=tk.X, pady=5)

            label = tk.Label(frame, text=f"{field}:", width=15, anchor="w")
            label.pack(side=tk.LEFT, padx=5)

            entry = tk.Entry(frame)
            entry.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=5)

            self.entries[field] = entry

    def get_values(self):
        """
        Obtiene los valores de los campos del formulario.

        Returns:
            dict: Un diccionario con los nombres de los campos como claves y sus valores como valores.
        """
        return {field: entry.get().strip() for field, entry in self.entries.items()}

    def clear(self):
        """Limpia todas las entradas del formulario."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)