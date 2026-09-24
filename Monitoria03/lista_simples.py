class No:
    def __init__(self, nome, gols=0):
        self.nome = nome
        self.gols = gols
        self.proximo = None


def adicionar_inicio(lista, nome, gols=0):
    no = No(nome, gols)

    if lista == None:
        lista = no
        return lista

    no.proximo = lista
    lista = no
    return lista


def adicionar_final(lista, nome, gols=0):
    no = No(nome, gols)

    if lista == None:
        lista = no
        return lista

    aux = lista
    while aux.proximo != None:
        aux = aux.proximo
    aux.proximo = no
    return lista


def percorrer(lista):
    aux = lista
    contador = 1

    if lista == None:
        print("Lista vazia")
        return

    while aux != None:
        print(contador, "=", aux.nome, "-", aux.gols, "gols")
        aux = aux.proximo
        contador = contador + 1


def media_gols(lista):
    aux = lista
    soma = 0
    quantidade = 0

    if lista == None:
        print("Lista vazia")
        return 0

    while aux != None:
        soma = soma + aux.gols
        quantidade = quantidade + 1
        aux = aux.proximo

    return soma / quantidade


def menu():
    print("1 - Adicionar jogador no início")
    print("2 - Adicionar jogador no final")
    print("3 - Listar jogadores")
    print("4 - Média de gols")
    print("5 - Sair")
    opc = int(input("Digite a opção:"))
    return opc


def main():
    opcao = 0
    lista = None

    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            nome = input("Nome do jogador:")
            gols = int(input("Gols marcados:"))
            lista = adicionar_inicio(lista, nome, gols)
        elif opcao == 2:
            nome = input("Nome do jogador:")
            gols = int(input("Gols marcados:"))
            lista = adicionar_final(lista, nome, gols)
        elif opcao == 3:
            percorrer(lista)
        elif opcao == 4:
            print("Média de gols:", media_gols(lista))


main()
