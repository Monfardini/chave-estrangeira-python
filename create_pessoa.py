class Pessoa():
    def __init__(self, _nome,_cpf, _id_pessoa, _id_cidade):
        self.nome = _nome
        self.cpf = _cpf
        self.id_pessoa = _id_pessoa
        self.id_cidade = _id_cidade
        
# Lista global para armazenar as cidades criadas
lista_pessoas = []

def criar_pessoas():
    lista_pessoas.append(Pessoa("Núbia", "423.678.658-56", 1, 1))
    
def mostrar_pessoas():
    for pessoa in lista_pessoas:
        print(f"Nome: {pessoa.nome}, CPF: {pessoa.cpf}, Estado: {pessoa.id_pessoa}")

# Chamando as funções
criar_pessoas()
mostrar_pessoas()