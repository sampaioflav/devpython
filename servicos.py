import tkinter as tk
from tkinter import messagebox
from db import conectar

def menu_servicos(root, frame_anterior=None):
    if frame_anterior:
        frame_anterior.destroy()

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    frame_interno = tk.Frame(frame)
    frame_interno.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame_interno, text="Cadastro de Serviços", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame_interno, text="Serviço:").grid(row=1, column=0, padx=10, pady=5)
    entry_servico = tk.Entry(frame_interno)
    entry_servico.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_interno, text="Preço:").grid(row=2, column=0, padx=10, pady=5)
    entry_preco = tk.Entry(frame_interno)
    entry_preco.grid(row=2, column=1, padx=10, pady=5)

    def cadastrar():
        servico = entry_servico.get()
        preco = entry_preco.get()
        conn, cursor = conectar()
        cursor.execute("INSERT INTO servicos (nome, preco) VALUES (?, ?)", (servico, preco))
        conn.commit()
        conn.close()
        listar()
        entry_servico.delete(0, tk.END)
        entry_preco.delete(0, tk.END)

    def editar():
        selecionado = lista.curselection()
        if selecionado:
            index = selecionado[0]
            id_servico = lista.get(index).split(" - ")[0]
            novo_servico = entry_servico.get()
            novo_preco = entry_preco.get()
            conn, cursor = conectar()
            cursor.execute("UPDATE servicos SET nome = ?, preco = ? WHERE id = ?", (novo_servico, novo_preco, id_servico))
            conn.commit()
            conn.close()
            listar()
            entry_servico.delete(0, tk.END)
            entry_preco.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Selecione um serviço para editar")

    def excluir():
        selecionado = lista.curselection()
        if selecionado:
            index = selecionado[0]
            id_servico = lista.get(index).split(" - ")[0]
            conn, cursor = conectar()
            cursor.execute("DELETE FROM servicos WHERE id = ?", (id_servico,))
            conn.commit()
            conn.close()
            listar()
        else:
            messagebox.showerror("Erro", "Selecione um serviço para excluir")

    tk.Button(frame_interno, text="Cadastrar", command=cadastrar).grid(row=3, column=0, pady=5)
    tk.Button(frame_interno, text="Editar", command=editar).grid(row=3, column=1, pady=5)
    tk.Button(frame_interno, text="Excluir", command=excluir).grid(row=3, column=2, padx=10, pady=5)

    lista = tk.Listbox(frame_interno, width=50)
    lista.grid(row=4, column=0, columnspan=3, pady=10)

    def voltar():
        from menu import mostrar_menu
        frame.destroy()
        mostrar_menu(root)

    tk.Button(frame_interno, text="Voltar ao Menu", command=voltar).grid(row=5, column=0, columnspan=3, pady=10)

    def listar():
        lista.delete(0, tk.END)
        conn, cursor = conectar()
        cursor.execute("SELECT * FROM servicos")
        for row in cursor.fetchall():
            lista.insert(tk.END, f"{row[0]} - {row[1]} - R${row[2]}")
        conn.close()

    listar()
