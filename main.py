from create_telefone import *
from create_email import *
from create_pessoa import *
from create_cidade import *

class Tabela():
    
    lista_total = lista_cidades + lista_pessoas

    # Mostrando a lista total
    for item in lista_total:
        if isinstance(item, Cidade,):
            print(f"Cidade: {item.nome}, Estado: {item.estado}, ID: {item.id_cidade}")
        if isinstance(item, Pessoa):
            print(f"Nome: {item.nome}, CPF: {item.cpf}, ID Pessoa: {item.id_pessoa}, ID Cidade: {item.id_cidade}")
        if isinstance(item, Email):
            print(f"Email: {item.email}")
        
        elif isinstance(item, Telefone):
            print(f"Telefone: {item.telefone}")
        
            
