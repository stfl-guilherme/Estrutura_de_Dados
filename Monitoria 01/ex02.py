class No:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao
        self.proximo = None
        self.anterior = None

def inserirfim(lista, nome, duracao):
    novaMusica = No(nome, duracao)

    if lista == None:
        lista = novaMusica
        lista.proximo = novaMusica
        lista.anterior = novaMusica
        return lista
    else:
        ultimo = lista.anterior
        novaMusica.proximo = lista
        novaMusica.anterior = ultimo
        ultimo.proximo = novaMusica
        lista.anterior = novaMusica
        return novaMusica

def inserirordenado(lista, nome, duracao):
    novaMusica = No(nome, duracao)

    if lista == None:
        lista = novaMusica
        lista.proximo = novaMusica
        lista.anterior = novaMusica
        return lista

    aux = lista
    while True:
        if duracao < aux.duracao:
            anterior = aux.anterior
            novaMusica.proximo = aux
            novaMusica.anterior = anterior
            anterior.proximo = novaMusica
            aux.anterior = novaMusica
            return novaMusica

        aux = aux.proximo
        if aux == lista:
            ultimo = lista.anterior
            novaMusica.proximo = lista
            novaMusica.anterior = ultimo
            ultimo.proximo = novaMusica
            lista.anterior = novaMusica
            return novaMusica

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
        print(aux.anterior.nome, "->", aux.nome, "->", aux.proximo.nome)
        aux = aux.proximo
        if aux == lista:
            return

def avancar(atual):
    return atual.proximo

def voltar(atual):
    return atual.anterior

def simularReproducao(atual, passos):
    for i in range(passos):
        if atual == None:
            return atual

        if i % 2 == 0:
            atual = avancar(atual)
            print(f"Passo {i + 1} (avancar): {atual.nome} - {atual.duracao}")
        else:
            atual = voltar(atual)
            print(f"Passo {i + 1} (voltar): {atual.nome} - {atual.duracao}")

    return atual

def menu():
    print("1 - Inserir no fim")
    print("2 - Inserir ordenado por duração")
    print("3 - Excluir")
    print("4 - Listar")
    print("5 - Simular 8 faixas")
    print("6 - Sair")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    lista = None
    atual = None
    opcao = 0

    while opcao != 6:
        opcao = menu()
        if opcao == 1:
            nome = input("Nome da música:")
            duracao = float(input("Duração:"))
            lista = inserirFim(lista, nome, duracao)
            if atual == None:
                atual = lista
        elif opcao == 2:
            nome = input("Nome da música:")
            duracao = float(input("Duração:"))
            lista = inserirOrdenado(lista, nome, duracao)
            if atual == None:
                atual = lista
        elif opcao == 3:
            nome = input("Nome da música para excluir:")
            if atual != None and atual.nome == nome:
                atual = None
            lista = excluir(lista, nome)
            if atual == None:
                atual = lista
        elif opcao == 4:
            listar(lista)
        elif opcao == 5:
            atual = simularReproducao(atual, 8)

main()
