'''
Implemente uma função que receba duas listas encadeadas de valores inteiros e retorne a lista resultante da concatenação 
das duas listas recebidas como parâmetros, isto é, após a concatenação, o último elemento da primeira lista deve apontar
para o primeiro elemento da segunda lista.
Esta função deve obedecer ao protótipo:

def concatenar(l1, l2):
'''
class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None

def concatenar(l1,l2):
    if l1 == None:
        return l2
    else:
        atual = l1
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = l2
        return l1

def listar_itens(lista):
    atual = lista
    while atual is not None:
        print("-", atual.dado)
        atual = atual.proximo

def main():
    l1 = No(1)
    l1.proximo = No(2)
    l1.proximo.proximo = No(3)
    l2 = No(4)
    l2.proximo = No(5)
    l2.proximo.proximo = No(6)
    listar_itens(concatenar(l1,l2))
main()