'''
Faça uma função que apresente a média dos dados na lista.
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

def calcular_media(lista):
    soma = 0
    divi = 0
    aux = lista
    while aux != None:
        soma += aux.dado
        divi += 1
        aux = aux.proximo
    return soma / divi

def menu2():
    print("<1> Adicionar no Inicio da lista")
    print("<2> Adicionar no Final da lista")
    opc = int(input("Digite a opção: "))
    return opc

def menu():
    print("-=-=-MENU-=-=-")
    print("<1> Inserir Elemento na lista")
    print("<2> Percorrer lista")
    print("<3> Calcular Média da lista")
    print("<4> Sair")
    opc = int(input("Digite a opção: "))
    return opc

def main():
    lista = None
    opc = 0

    while opc != 4:
        opc = menu()
        if opc == 1:
            dado = int(input("Digite o item para adicionar: "))
            lista = adicionar_elemento(lista, dado)
        elif opc == 2:
            percorrer_lista(lista)
        elif opc == 3:
            media = calcular_media(lista)
            print("A média dos itens é: ",media)
        elif opc == 4:
            print("Saindo...")
main()