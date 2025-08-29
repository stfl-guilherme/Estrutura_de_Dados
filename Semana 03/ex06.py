'''
implemente uma função que calcule a média aritmética dos valores armazenados. Esta função deve ter o protótipo:
def lista_calcula_media(lst):
'''

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

def lista_calcula_media(lista):
    atual = lista
    soma = 0
    valores = 0
    while atual is not None:
        soma += atual.dado
        valores += 1
        atual = atual.proximo
    return (soma / valores)

def main():
    lista = No(7)
    lista.proximo = No(9)
    lista.proximo.proximo = No(5)

    print("Média das notas: ", lista_calcula_media(lista))

main()