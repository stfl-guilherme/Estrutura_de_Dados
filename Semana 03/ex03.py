'''
Implemente uma função que tenha como valor de retorno a referência do último nó de uma lista encadeada. 
Esta função deve obedecer ao protótipo:

def ultimo(lista):
'''
class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None

def ultimo(lista):
    atual = lista
    while atual is not None:
        if atual.proximo == None:
            return atual.dado
        atual = atual.proximo

def main():
    lista = No(1)
    lista.proximo = No(2)
    lista.proximo.proximo = No(3)
    print("Ultimo nó: ", ultimo(lista))

main()