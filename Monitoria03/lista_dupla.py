class NoDuplo:
    def __init__(self, nome):
        self.nome = nome
        self.anterior = None
        self.proximo = None


def adicionar_inicio(lista_inicio, lista_fim, nome):
    novo = NoDuplo(nome)

    if lista_inicio == None:
        lista_inicio = novo
        lista_fim = novo
        return lista_inicio, lista_fim

    novo.proximo = lista_inicio
    lista_inicio.anterior = novo
    lista_inicio = novo
    return lista_inicio, lista_fim


def percorrer_frente(lista_inicio):
    aux = lista_inicio
    contador = 1

    if lista_inicio == None:
        print("Lista vazia")
        return

    while aux != None:
        print(contador, "=", aux.nome)
        aux = aux.proximo
        contador = contador + 1


def percorrer_tras(lista_fim):
    aux = lista_fim
    contador = 1

    if lista_fim == None:
        print("Lista vazia")
        return

    while aux != None:
        print(contador, "=", aux.nome)
        aux = aux.anterior
        contador = contador + 1


def menu():
    print("1 - Adicionar jogador")
    print("2 - Listar do primeiro ao último")
    print("3 - Listar do último ao primeiro")
    print("4 - Sair")
    opc = int(input("Digite a opção:"))
    return opc


def main():
    opcao = 0
    lista_inicio = None
    lista_fim = None

    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            nome = input("Nome do jogador:")
            lista_inicio, lista_fim = adicionar_inicio(lista_inicio, lista_fim, nome)
        elif opcao == 2:
            percorrer_frente(lista_inicio)
        elif opcao == 3:
            percorrer_tras(lista_fim)


main()
