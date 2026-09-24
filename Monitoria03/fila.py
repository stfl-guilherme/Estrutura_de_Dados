class No:
    def __init__(self, usuario, tempo_espera=0):
        self.usuario = usuario
        self.tempo_espera = tempo_espera
        self.proximo = None
        self.anterior = None


def enfileirar(fila_inicio, fila_fim, usuario, tempo_espera=0):
    novo = No(usuario, tempo_espera)

    if fila_inicio == None:
        fila_inicio = novo
        fila_fim = novo
        return fila_inicio, fila_fim

    fila_fim.proximo = novo
    novo.anterior = fila_fim
    fila_fim = novo
    return fila_inicio, fila_fim


def desenfileirar(fila_inicio, fila_fim):
    if fila_inicio == None:
        print("Fila vazia")
        return None, None

    if fila_inicio == fila_fim:
        return None, None

    fila_inicio = fila_inicio.proximo
    fila_inicio.anterior = None
    return fila_inicio, fila_fim


def percorrer(fila_inicio):
    aux = fila_inicio
    contador = 1

    if fila_inicio == None:
        print("Fila vazia")
        return

    while aux != None:
        print(contador, "=", aux.usuario, "-", aux.tempo_espera, "min")
        contador = contador + 1
        aux = aux.proximo


def frente(fila_inicio):
    if fila_inicio == None:
        print("Fila vazia")
        return None
    return fila_inicio.usuario


def esta_vazia(fila_inicio):
    return fila_inicio == None


def tamanho(fila_inicio):
    aux = fila_inicio
    contador = 0

    while aux != None:
        contador = contador + 1
        aux = aux.proximo

    return contador


def tempo_medio_espera(fila_inicio):
    aux = fila_inicio
    soma = 0
    quantidade = 0

    if fila_inicio == None:
        print("Fila vazia")
        return 0

    while aux != None:
        soma = soma + aux.tempo_espera
        quantidade = quantidade + 1
        aux = aux.proximo

    return soma / quantidade


def menu():
    print("1 - Enfileirar")
    print("2 - Desenfileirar (atender)")
    print("3 - Listar fila")
    print("4 - Próximo a ser atendido")
    print("5 - Fila está vazia?")
    print("6 - Tamanho da fila")
    print("7 - Tempo médio de espera")
    print("8 - Sair")
    opc = int(input("Digite uma opção:"))
    return opc


def main():
    opcao = 0
    fila_fim = None
    fila_inicio = None

    while opcao != 8:
        opcao = menu()
        if opcao == 1:
            usuario = input("Nome do usuário:")
            tempo = int(input("Tempo de espera (min):"))
            fila_inicio, fila_fim = enfileirar(fila_inicio, fila_fim, usuario, tempo)
        elif opcao == 2:
            print("Atendendo:", frente(fila_inicio))
            fila_inicio, fila_fim = desenfileirar(fila_inicio, fila_fim)
        elif opcao == 3:
            percorrer(fila_inicio)
        elif opcao == 4:
            print("Próximo:", frente(fila_inicio))
        elif opcao == 5:
            print("Vazia?", esta_vazia(fila_inicio))
        elif opcao == 6:
            print("Tamanho:", tamanho(fila_inicio))
        elif opcao == 7:
            print("Tempo médio:", tempo_medio_espera(fila_inicio))


main()
