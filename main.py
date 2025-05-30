import tkinter as tk
from db import criar_tabelas
from menu import mostrar_menu

if __name__ == "__main__":
    criar_tabelas()
    root = tk.Tk()
    root.title("Sistema de Agendamento")

    # Ocupa toda a tela, mas mantém barra de título
    largura = root.winfo_screenwidth()
    altura = root.winfo_screenheight()
    root.geometry(f"{largura}x{altura}")

    mostrar_menu(root)
    root.mainloop()
