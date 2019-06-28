import os

def cadastrar(nome,telefone):
    arq = open('lista_telefonica.txt','a')
    arq.write(nome)
    arq.write(' - ')
    arq.write(telefone)
    arq.write('\n')
    arq.close()
    backup = open('lista_telefonica_backup.txt','a')
    backup.write(nome)
    backup.write(' - ')
    backup.write(telefone)
    backup.write('\n')
    backup.close()

def listar():
    arq = open('lista_telefonica.txt','r')
    for linha in arq:
        linha = linha.rstrip() #tira uma linha em branco causada pelo print
        print(linha)
    arq.close()

def apagar(telefone):
    with open('lista_telefonica.txt','r+') as arquivo:
        novo_arq = arquivo.readlines()
        arquivo.seek(0)
        for linha in novo_arq:
            if telefone not in linha:
                arquivo.write(linha)
        arquivo.truncate()

