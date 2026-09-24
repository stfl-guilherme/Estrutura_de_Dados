class NoDuploCircular:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


def adicionar_inicio(lista, dado):
    no = NoDuploCircular(dado)

    if lista == None:
        no.proximo = no
        no.anterior = no
        lista = no
        return lista

    no.proximo = lista
    no.anterior = lista.anterior
    lista.anterior.proximo = no
    lista.anterior = no
    lista = no
    return lista


def adicionar_final(lista, dado):
    no = NoDuploCircular(dado)

    if lista == None:
        no.proximo = no
        no.anterior = no
        lista = no
        return lista

    no.anterior = lista.anterior
    no.proximo = lista
    lista.anterior.proximo = no
    lista.anterior = no
    return lista


def percorrer_frente(lista, quantidade):
    if lista == None:
        print("Lista vazia")
        return

    aux = lista
    for i in range(quantidade):
        print(i + 1, "=", aux.dado)
        aux = aux.proximo


def percorrer_tras(lista, quantidade):
    if lista == None:
        print("Lista vazia")
        return

    aux = lista.anterior
    for i in range(quantidade):
        print(i + 1, "=", aux.dado)
        aux = aux.anterior


def remover(lista, dado):
    if lista == None:
        print("Lista vazia")
        return lista

    aux = lista
    while True:
        if aux.dado == dado:
            if aux.proximo == aux:  # único elemento
                return None
            if aux == lista:  # é a cabeça, precisa mover antes de desligar o nó
                lista = lista.proximo
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            return lista

        aux = aux.proximo
        if aux == lista:  # deu a volta completa e não achou
            print("Dado não encontrado")
            return lista


def menu():
    print("1 - Adicionar no início")
    print("2 - Adicionar no final")
    print("3 - Percorrer para frente")
    print("4 - Percorrer para trás")
    print("5 - Remover")
    print("6 - Sair")
    opc = int(input("Digite a opção:"))
    return opc


def main():
    opcao = 0
    lista = None

    while opcao != 6:
        opcao = menu()
        if opcao == 1:
            dado = int(input("Digite um dado:"))
            lista = adicionar_inicio(lista, dado)
        elif opcao == 2:
            dado = int(input("Digite um dado:"))
            lista = adicionar_final(lista, dado)
        elif opcao == 3:
            quantidade = int(input("Quantos passos:"))
            percorrer_frente(lista, quantidade)
        elif opcao == 4:
            quantidade = int(input("Quantos passos:"))
            percorrer_tras(lista, quantidade)
        elif opcao == 5:
            dado = int(input("Dado para remover:"))
            lista = remover(lista, dado)


main()
