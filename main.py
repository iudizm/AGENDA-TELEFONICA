from cabecalho import cabecalho
import os
from funx import *

print(cabecalho())
print("\n=== AGENDA TELEFÔNICA ===")

while True:

    escolha = input('\n ===MENU===\n 1 - add telefone\n 2 - listar telefones\n 3 - apagar telefone\n 0 - SAIR\n\n DIGITE SUA OPÇÃO: ')

    if escolha == '1':
        try:
            nome = input("Nome do contato: ")
            telefone = input('Telefone do contato(9 algarismos): ')
            cadastrar(nome, telefone)
        except TypeError:
            print("Erro de digitação, tente novamente")

    elif escolha == '2':
        try:
            listar()
        except FileNotFoundError:
            print('nao existe lista telefonica ainda!\n Adicione um contato para que ele seja listado!')

    elif escolha == '3':
        
            telefone = input('\nPara que não ocorram erros, por favor digite o número a ser apagado\nCertifique-se de digitar conforme o número na listagem:  ')
            apagar(telefone)
            print('\nCONTATO APAGADO COM SUCESSO')
    elif escolha == '0':
        sair = input('DESEJA SAIR DO PROGRAMA??? (S/N)')
        
        if sair.lower() == 's':
            break
        elif sair.lower() == 'n':
            print('ok entao')
        else:
            print('Por favor, (S/N)')

    else:
        print('Digite uma opção válida')
