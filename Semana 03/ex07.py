'''
Implemente uma função que altere uma lista, de forma que os valores positivos fiquem negativos e os negativos fiquem positivos.
Esta função deve ter o protótipo:
def lista_altera(lst):
'''

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

def lista_altera(lista):
    atual = lista
    while atual is not None:
        atual.dado *= -1
        atual = atual.proximo
    return lista

def listar_itens(lista):
    atual = lista
    while atual is not None:
        print("-", atual.dado)
        atual = atual.proximo

def main():
    lista = No(1)
    lista.proximo = No(-2)
    lista.proximo.proximo = No(4)
    lista.proximo.proximo.proximo = No(-3)
    lista.proximo.proximo.proximo.proximo = No(5)
    lista.proximo.proximo.proximo.proximo.proximo = No(9)

    print("lista normal")
    listar_itens(lista)
    lista = lista_altera(lista)
    print("lista alterada")
    listar_itens(lista)

main()