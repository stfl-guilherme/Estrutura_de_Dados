import random

class No:
    def __init__(self, nome, status):
        self.nome = nome
        self.status = status
        self.proximo = None
        self.anterior = None

def inserir(lista, nome, status):
    novoModulo = No(nome, status)

    if lista == None:
        lista = novoModulo
        lista.proximo = novoModulo
        lista.anterior = novoModulo
        return lista
    else:
        ultimo = lista.anterior
        novoModulo.proximo = lista
        novoModulo.anterior = ultimo
        ultimo.proximo = novoModulo
        lista.anterior = novoModulo
        return novoModulo

def excluir(lista, nome):
    aux = lista

    while True:
        if aux.nome == nome:
            if aux.proximo == aux:
                return None

            elif aux == lista:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return lista.proximo

            elif aux.proximo == lista:
                aux.anterior.proximo = lista
                aux.proximo.anterior = aux.anterior
                return lista

            else:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return lista

        aux = aux.proximo
        if aux == lista:
            print("Elemento não encontrado")
            return lista

def listar(lista):
    aux = lista

    if lista == None:
        print("Lista vazia")
        return

    while True:
        print(aux.anterior.nome, "->", aux.nome, "->", aux.proximo.nome, "-", aux.status)
        aux = aux.proximo
        if aux == lista:
            return

def inspecionar(lista):
    aux = lista

    if lista == None:
        print("Lista vazia")
        return

    while True:
        if random.random() < 0.5:
            aux.status = "danificado"
            print(f"Inspeção: {aux.nome} marcado como danificado")
        else:
            print(f"Inspeção: {aux.nome} ok")
        aux = aux.proximo
        if aux == lista:
            return

def reparar(lista):
    aux = lista

    if lista == None:
        print("Lista vazia")
        return

    while True:
        if aux.status == "danificado":
            aux.status = "funcional"
            print(f"Reparo: {aux.nome} foi reparado")
        aux = aux.proximo
        if aux == lista:
            return

def menu():
    print("1 - Inserir módulo")
    print("2 - Excluir módulo")
    print("3 - Listar módulos")
    print("4 - Inspecionar anel")
    print("5 - Reparar anel")
    print("6 - Sair")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    lista = None
    opcao = 0

    while opcao != 6:
        opcao = menu()
        if opcao == 1:
            nome = input("Nome do módulo:")
            lista = inserir(lista, nome, "funcional")
        elif opcao == 2:
            nome = input("Nome do módulo para excluir:")
            lista = excluir(lista, nome)
        elif opcao == 3:
            listar(lista)
        elif opcao == 4:
            inspecionar(lista)
        elif opcao == 5:
            reparar(lista)

main()
