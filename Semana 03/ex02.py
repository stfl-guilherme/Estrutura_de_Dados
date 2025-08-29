'''
Considere listas encadeadas de valores inteiros e implemente uma função para retornar o número de 
nós da lista que possuem o campo info com valores maiores do que n (informado pelo usuário).
Esta função deve obedecer ao protótipo:

def maiores(lst, n):
'''

class No:
    def __init__ (self, dado):
        self.dado = dado
        self.proximo = None

def maiores(lista, n):
    atual = lista
    contador = 0
    while atual is not None:
        if atual.dado > n:
            contador += 1
        atual = atual.proximo
    return contador

def main():
    lista = No(12)
    lista.proximo = No(23)
    lista.proximo.proximo = No(2)
    
    n = int(input("Digite um valor para encontar valores maiores na lista oculta: "))
    resposta = maiores(lista, n)
    print("O codigo encontrou",resposta,"valores maiores que ",n)
main()