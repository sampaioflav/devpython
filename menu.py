import tkinter as tk
import clientes
import servicos
import agendamentos

def mostrar_menu(root, frame=None):
    if frame:
        frame.destroy()

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)  # Frame ocupa toda janela

    container = tk.Frame(frame)
    container.pack(expand=True)  # Container centralizado verticalmente

    tk.Label(container, text="Menu Principal", font=("Arial", 16)).pack(pady=(0, 20))

    btn_clientes = tk.Button(container, text="Clientes", width=20, command=lambda: clientes.menu_clientes(root, frame))
    btn_clientes.pack(pady=5)

    btn_servicos = tk.Button(container, text="Serviços", width=20, command=lambda: servicos.menu_servicos(root, frame))
    btn_servicos.pack(pady=5)

    btn_agendamentos = tk.Button(container, text="Agendamentos", width=20, command=lambda: agendamentos.menu_agendamentos(root, frame))
    btn_agendamentos.pack(pady=5)

    btn_sair = tk.Button(container, text="Sair", width=20, command=root.quit)
    btn_sair.pack(pady=20)



# Exemplo de execução direta:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Agendamento")
    root.geometry("400x300")
    mostrar_menu(root)
    root.mainloop()
