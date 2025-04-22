# main.py
import logging
from ui.main_ui import MainUI
from tkinter import Tk

logging.basicConfig(
    filename="pos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Iniciando sistema POS")
    root = Tk()
    app = MainUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()