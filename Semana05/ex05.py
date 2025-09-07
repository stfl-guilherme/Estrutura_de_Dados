'''
Modifique a classe ListaEncadeada do exercício anterior para incluir um método adicionar_final(dado) que adiciona um novo nó no final da lista.
Teste a funcionalidade adicionando elementos no início e no final e percorrendo a lista.
'''

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

def adicionar_elemento(lista, dado):
    opc = menu2()
    if opc == 1:
        novo = No(dado)
        if lista == None:
            return novo
        novo.proximo = lista
        return novo
    elif opc == 2:
        novo = No(dado)
        aux = lista
        #verirficar se está vazia
        if lista == None:
            return novo
        while aux.proximo != None:
            aux = aux.proximo
        aux.proximo = novo
        return lista

def percorrer_lista(lista):
    aux = lista
    if aux == None:
        print("Lista vazia")
        return
    while aux != None:
        print("- ", aux.dado)
        aux = aux.proximo

def menu2():
    print("<1> Adicionar no Inicio da lista")
    print("<2> Adicionar no Final da lista")
    opc = int(input("Digite a opção: "))
    return opc

def menu():
    print("-=-=-MENU-=-=-")
    print("<1> Inserir Elemento na lista")
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
            lista = adicionar_elemento(lista, dado)
        elif opc == 2:
            percorrer_lista(lista)

main()