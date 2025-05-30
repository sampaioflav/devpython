import tkinter as tk
from tkinter import messagebox
from db import conectar
from validations import validar_nome

def menu_clientes(root, frame_anterior=None):
    if frame_anterior:
        frame_anterior.destroy()

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    conteudo = tk.Frame(frame)
    conteudo.pack(expand=True)

    tk.Label(conteudo, text="Cadastro de clientes", font=("Arial", 16)).pack(pady=10)

    linha_nome = tk.Frame(conteudo)
    linha_nome.pack(pady=5)
    tk.Label(linha_nome, text="Nome:", width=10, anchor="e").pack(side="left")
    entry_nome = tk.Entry(linha_nome, width=30)
    entry_nome.pack(side="left")

    linha_telefone = tk.Frame(conteudo)
    linha_telefone.pack(pady=5)
    tk.Label(linha_telefone, text="Telefone:", width=10, anchor="e").pack(side="left")
    entry_telefone = tk.Entry(linha_telefone, width=30)
    entry_telefone.pack(side="left")

    linha_email = tk.Frame(conteudo)
    linha_email.pack(pady=5)
    tk.Label(linha_email, text="Email:", width=10, anchor="e").pack(side="left")
    entry_email = tk.Entry(linha_email, width=30)
    entry_email.pack(side="left")

    def cadastrar():
        nome = entry_nome.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        if validar_nome(nome):
            conn, cursor = conectar()
            cursor.execute(
                "INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)",
                (nome, telefone, email)
            )
            conn.commit()
            conn.close()
            listar()
            entry_nome.delete(0, tk.END)
            entry_telefone.delete(0, tk.END)
            entry_email.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Nome inválido")

    def editar():
        selecionado = lista.curselection()
        if selecionado:
            index = selecionado[0]
            id_cliente = lista.get(index).split(" - ")[0]
            novo_nome = entry_nome.get()
            novo_telefone = entry_telefone.get()
            novo_email = entry_email.get()
            if validar_nome(novo_nome):
                conn, cursor = conectar()
                cursor.execute(
                    "UPDATE clientes SET nome = ?, telefone = ?, email = ? WHERE id = ?",
                    (novo_nome, novo_telefone, novo_email, id_cliente)
                )
                conn.commit()
                conn.close()
                listar()
                entry_nome.delete(0, tk.END)
                entry_telefone.delete(0, tk.END)
                entry_email.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Nome inválido")
        else:
            messagebox.showerror("Erro", "Selecione um cliente para editar")

    def excluir():
        selecionado = lista.curselection()
        if selecionado:
            index = selecionado[0]
            id_cliente = lista.get(index).split(" - ")[0]
            conn, cursor = conectar()
            cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
            conn.commit()
            conn.close()
            listar()
            entry_nome.delete(0, tk.END)
            entry_telefone.delete(0, tk.END)
            entry_email.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Selecione um cliente para excluir")

    def listar():
        lista.delete(0, tk.END)
        conn, cursor = conectar()
        cursor.execute("SELECT * FROM clientes")
        for row in cursor.fetchall():
            lista.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")
        conn.close()

    linha_botoes = tk.Frame(conteudo)
    linha_botoes.pack(pady=10)
    tk.Button(linha_botoes, text="Cadastrar", command=cadastrar, width=12).pack(side="left", padx=5)
    tk.Button(linha_botoes, text="Editar", command=editar, width=12).pack(side="left", padx=5)
    tk.Button(linha_botoes, text="Excluir", command=excluir, width=12).pack(side="left", padx=5)

    lista = tk.Listbox(conteudo, width=70)
    lista.pack(pady=10)

    def voltar():
        from menu import mostrar_menu
        frame.destroy()
        mostrar_menu(root)

    tk.Button(conteudo, text="Voltar ao Menu", command=voltar, width=30).pack(pady=10)

    listar()
