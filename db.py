import sqlite3

def conectar():
    conn = sqlite3.connect("clinica.db")
    cursor = conn.cursor()
    return conn, cursor

def criar_tabelas():
    conn, cursor = conectar()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        descricao TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL,
        id_servico INTEGER NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES clientes(id),
        FOREIGN KEY (id_servico) REFERENCES servicos(id)
    )
    """)
    conn.commit()
    conn.close()

def executar_query(sql, params=()):
    conn, cursor = conectar()
    cursor.execute(sql, params)
    conn.commit()
    conn.close()

def fetchall_query(sql, params=()):
    conn, cursor = conectar()
    cursor.execute(sql, params)
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def fetchone_query(sql, params=()):
    conn, cursor = conectar()
    cursor.execute(sql, params)
    resultado = cursor.fetchone()
    conn.close()
    return resultado
