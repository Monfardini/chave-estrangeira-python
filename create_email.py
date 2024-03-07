class Email:
    def __init__(self, _email):
        self.email = _email

# Lista global para armazenar e-mails
lista_emails = []

def criar_emails():
    lista_emails.append(Email("exemplo1@teste.com"))

def mostrar_emails():
    # Esta função itera sobre a lista de e-mails e imprime cada um
    for email_obj in lista_emails:
        print(f"Email: {email_obj.email}")

# Chamando as funções para demonstração
criar_emails()
mostrar_emails()

