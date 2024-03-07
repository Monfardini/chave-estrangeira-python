class Cidade:
    def __init__(self, nome, estado, id_cidade):
        self.nome = nome
        self.estado = estado
        self.id_cidade = id_cidade

# Lista global para armazenar as cidades criadas
lista_cidades = []

def criar_cidades():
    lista_cidades.append(Cidade("São Paulo", "SP", 1))
    
def mostrar_cidades():
    for cidade in lista_cidades:
        print(f"ID: {cidade.id_cidade}, Nome: {cidade.nome}, Estado: {cidade.estado}")

# Chamando as funções
criar_cidades()
mostrar_cidades()