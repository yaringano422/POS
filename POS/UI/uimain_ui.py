# ui/main_ui.py
import tkinter as tk
from tkinter import ttk
from services.inventory import InventoryService
from services.sales import SalesService
from services.users import UserService
from data.database import get_db

class MainUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema POS")
        self.db = next(get_db())
        self.inventory_service = InventoryService(self.db)
        self.sales_service = SalesService(self.db)
        self.user_service = UserService(self.db)
        self.current_user = None

        self.login_screen()

    def login_screen(self):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame, text="Usuario:").pack()
        username_entry = tk.Entry(frame)
        username_entry.pack()

        def login():
            username = username_entry.get()
            user = self.db.query(User).filter(User.username == username).first()
            if user:
                self.current_user = user
                frame.destroy()
                self.main_menu()
            else:
                tk.Label(frame, text="Usuario no encontrado").pack()

        tk.Button(frame, text="Iniciar sesión", command=login).pack()

    def main_menu(self):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Inventario", command=self.show_inventory).pack()
        tk.Button(frame, text="Ventas", command=self.show_sales).pack()
        tk.Button(frame, text="Salir", command=self.root.quit).pack()

    def show_inventory(self):
        categories = self.inventory_service.get_all_categories()
        print(categories)  # Aquí se puede construir una vista gráfica para mostrar categorías y productos.