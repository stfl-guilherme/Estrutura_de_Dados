class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


def empilhar(pilha, dado):
    no = No(dado)
    if pilha == None:
        pilha = no
        return pilha
    no.proximo = pilha
    pilha = no
    return pilha


def desempilhar(pilha):
    if pilha == None:
        print("Pilha vazia")
        return None
    return pilha.proximo


def percorrer(pilha):
    aux = pilha
    contador = 1

    if pilha == None:
        print("Pilha vazia")
        return

    while aux != None:
        print(contador, "=", aux.dado)
        aux = aux.proximo
        contador = contador + 1


def topo(pilha):
    if pilha == None:
        print("Pilha vazia")
        return None
    return pilha.dado


def esta_vazia(pilha):
    return pilha == None


def tamanho(pilha):
    aux = pilha
    contador = 0

    while aux != None:
        contador = contador + 1
        aux = aux.proximo

    return contador


def media(pilha):
    aux = pilha
    soma = 0
    quantidade = 0

    if pilha == None:
        print("Pilha vazia")
        return 0

    while aux != None:
        soma = soma + aux.dado
        quantidade = quantidade + 1
        aux = aux.proximo

    return soma / quantidade


def menu():
    print("1 - Empilhar")
    print("2 - Desempilhar")
    print("3 - Listar pilha")
    print("4 - Ver topo")
    print("5 - Pilha está vazia?")
    print("6 - Tamanho da pilha")
    print("7 - Média dos valores")
    print("8 - Sair")
    opc = int(input("Digite a opção:"))
    return opc


def main():
    opcao = 0
    pilha = None

    while opcao != 8:
        opcao = menu()
        if opcao == 1:
            dado = int(input("Digite um valor:"))
            pilha = empilhar(pilha, dado)
        elif opcao == 2:
            pilha = desempilhar(pilha)
        elif opcao == 3:
            percorrer(pilha)
        elif opcao == 4:
            print("Topo:", topo(pilha))
        elif opcao == 5:
            print("Vazia?", esta_vazia(pilha))
        elif opcao == 6:
            print("Tamanho:", tamanho(pilha))
        elif opcao == 7:
            print("Média:", media(pilha))


main()
