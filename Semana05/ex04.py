'''
Implemente uma lista encadeada simples em Python. Crie uma classe No para representar um nó da lista (com dado e proximo) e uma classe ListaEncadeada 
com métodos para adicionar um nó no início (adicionar_inicio) e percorrer a lista (percorrer). Adicione alguns elementos e imprima a lista.
'''

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

def adicionar_inicio(lista, dado):
    novo = No(dado)
    if lista == None:
        return novo
    novo.proximo = lista
    return novo

def percorrer_lista(lista):
    aux = lista
    if aux == None:
        print("Lista vazia")
    while aux != None:
        print("- ", aux.dado)
        aux = aux.proximo

def menu():
    print("-=-=-MENU-=-=-")
    print("<1> Inserir no Inicio da lista")
    print("<2> Percorrer lista")
    opc = int(input("Digite a opção: "))
    return opc

def main():
    lista = None
    opc = 0

    while opc != 3:
        opc = menu()
        if opc == 1:
            dado = int(input("Digite o item para adicionar: "))
            lista = adicionar_inicio(lista, dado)
        elif opc == 2:
            percorrer_lista(lista)

main()