from cabecalho import cabecalho
import os
from funx import *

print(cabecalho())
print("\n=== AGENDA TELEFÔNICA DO NOKIA TIJOLÃO ===")

escolha = input('\n ===MENU===\n 1 - add telefone\n 2 - listar telefones\n 3 - apagar telefone\n 0 - SAIR\n\n DIGITE SUA OPÇÃO: ')

if escolha == '1':
    nome = input("Nome do contato: ")
    telefone = input('Telefone do contato: ')
    cadastrar(nome, telefone)

if escolha == '2':
    try:
        listar()
    except FileNotFoundError:
        print('nao existe lista telefonica ainda!')
