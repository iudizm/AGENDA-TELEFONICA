import os

def cadastrar(nome,telefone):
    arq = open('lista_telefonica.txt','a')
    arq.write(nome)
    arq.write(' - ')
    arq.write(telefone)
    arq.write('\n')
    arq.close()
    

def listar():
    arq = open('lista_telefonica.txt','r')
    for linha in arq:
        linha = linha.rstrip() #tira uma linha em branco causada pelo print
        print(linha)
    arq.close()