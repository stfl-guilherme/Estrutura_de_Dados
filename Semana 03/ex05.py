'''
Implemente uma função que insira elementos sempre ao final da lista. Esta função deve ter o protótipo:
def lista_insere_final(lst, valor):
'''

class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None

def menu():
    print("1. Inserir item")
    print("2. Lista itens")
    print("3. Sair")
    opc = int(input("Digite a opção: "))
    return opc

def lista_insere_final(lista, valor):
    novo = No(valor)
    if lista is None:
        return novo
    else:
        atual = lista
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo
        return lista

def listar_itens(lista):
    atual = lista
    if atual == None:
        print("lista vazia")
    else: 
        while atual is not None:
            print("-", atual.dado)
            atual = atual.proximo

def main():
    lista = None
    opc = 0
    while opc != 3:
        opc = menu()
        if opc == 1:
            valor = int(input("Digite um valor para inserir: "))
            lista = lista_insere_final(lista, valor)
        elif opc == 2:
            listar_itens(lista)
        else:
            print("Encerrando Algoritimo...")
main()