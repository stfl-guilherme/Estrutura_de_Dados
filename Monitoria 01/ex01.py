class No:
    def __init__(self, nome):
        self.nome = nome
        self.plantoes = 0
        self.proximo = None
        self.anterior = None

def inserir(lista, nome):
    novoFuncionario = No(nome)

    if lista == None:
        lista = novoFuncionario
        lista.proximo = novoFuncionario
        lista.anterior = novoFuncionario
        return lista
    else:
        ultimo = lista.anterior
        novoFuncionario.proximo = lista
        novoFuncionario.anterior = ultimo
        ultimo.proximo = novoFuncionario
        lista.anterior = novoFuncionario
        return novoFuncionario

def listar(lista):
    aux = lista

    if lista == None:
        print("Lista vazia")
        return

    while True:
        print(aux.anterior.nome, "->", aux.nome, "->", aux.proximo.nome, "- plantoes:", aux.plantoes)
        aux = aux.proximo
        if aux == lista:
            return

def excluir(lista, atual, nome):
    aux = lista

    while True:
        if aux.nome == nome:
            if aux.proximo == aux:
                return None, None

            elif aux == lista:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                if atual == aux:
                    atual = aux.proximo
                return lista.proximo, atual

            elif aux.proximo == lista:
                aux.anterior.proximo = lista
                aux.proximo.anterior = aux.anterior
                if atual == aux:
                    atual = aux.proximo
                return lista, atual

            else:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                if atual == aux:
                    atual = aux.proximo
                return lista, atual

        aux = aux.proximo
        if aux == lista:
            print("Elemento não encontrado")
            return lista, atual

def proximoMenorPlantoes(atual):
    aux = atual.proximo
    menor = atual

    while aux != atual:
        if aux.plantoes < menor.plantoes:
            menor = aux
        aux = aux.proximo

    return menor

def simularSorteios(lista, atual, n):
    for i in range(n):
        if lista == None:
            return atual

        escolhido = proximoMenorPlantoes(atual)
        escolhido.plantoes += 1
        atual = escolhido.proximo
        print(f"Sorteio {i + 1}: {escolhido.nome} - plantoes: {escolhido.plantoes}")

    return atual

def menu():
    print("1 - Inserir")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Simular 10 sorteios")
    print("5 - Sair")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    lista = None
    atual = None
    opcao = 0

    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            nome = input("Digite o nome do funcionário:")
            lista = inserir(lista, nome)
            if atual == None:
                atual = lista
        elif opcao == 2:
            listar(lista)
        elif opcao == 3:
            nome = input("Digite o nome do funcionário para excluir:")
            lista, atual = excluir(lista, atual, nome)
        elif opcao == 4:
            atual = simularSorteios(lista, atual, 10)

main()
