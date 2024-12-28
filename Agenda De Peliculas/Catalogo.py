#Con Esta Parte Del Codigo Se Inicia La Aplicacion

import tkinter as tk
from cliente.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title("Catalogo")
    root.resizable(0,0)
    
    barra_menu(root)
    
    app = Frame(root = root)
    
    app.mainloop()
    
    


if __name__ == "__main__":
    main()
    
