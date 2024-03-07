class Telefone:
    def __init__(self, _telefone):
        self.telefone= _telefone
        
#lista global para telefones
lista_telefones = []

def criar_telefones():
    lista_telefones.append(Telefone("+55 11 1234-5678"))

def mostrar_telefones():
    # Esta função itera sobre a lista de telefones e imprime cada um
    for telefone_obj in lista_telefones:
        print(f"Telefone: {telefone_obj.telefone}")

# Chamando as funções para demonstração
criar_telefones()
mostrar_telefones()

