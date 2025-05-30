import re
from datetime import datetime

def validar_nome(nome):
    return len(nome.strip().split()) >= 2

def validar_telefone(telefone):
    telefone_limpo = re.sub(r'\D', '', telefone)
    return len(telefone_limpo) in [10, 11]

def formatar_telefone(telefone):
    telefone_limpo = re.sub(r'\D', '', telefone)
    if len(telefone_limpo) == 10:
        return f"({telefone_limpo[:2]}){telefone_limpo[2:6]}-{telefone_limpo[6:]}"
    elif len(telefone_limpo) == 11:
        return f"({telefone_limpo[:2]}){telefone_limpo[2:7]}-{telefone_limpo[7:]}"
    return telefone

def validar_email(email):
    return re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email)

def validar_data(data):
    try:
        data_formatada = datetime.strptime(data, "%d/%m/%Y")
        return data_formatada.date() >= datetime.now().date()
    except ValueError:
        return False

def validar_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False
