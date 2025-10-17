"""
Simular uma sala de partidas em que jogadores entram numa fila. A cada rodada, 
o jogador da frente participa da partida e volta para o fim da fila, mantendo 
o rodízio contínuo.

Adicionar jogador ao final da fila
Remover jogador específico (se alguém saiu da sala)
Simular 1 rodada (o primeiro joga e vai para o fim)
Simular N rodadas (executa o item 3 repetido N vezes, exibindo a ordem a cada rodada)
Mostrar fila (da posição 1 → fim)
Mostrar próximo a jogar (frente da fila)
Limpar fila
Sair
"""
class No:
    def __init__(self, jogador): 
        self.jogador = jogador
        self.proximo = None
        self.anterior = None

def inserir(lista, jogador):
    novo = No(jogador)
    if lista is None:
        return novo
    aux = lista
    while aux.proximo is not None:
        aux = aux.proximo
    aux.proximo = novo
    novo.anterior = aux
    return lista

def listar(lista):
    aux = lista
    if aux is None:
        print("Sem jogadores na fila")
        return
    print("\nFila de jogadores:")
    count = 0
    while aux is not None:
        count += 1
        print(count, "º jogador:", aux.jogador)
        aux = aux.proximo
    print("\n")

def remover_padrao(lista):
    if lista is None:
        print("Sem jogadores na fila")
        return None
    aux = lista
    lista = lista.proximo
    if lista is not None:
        lista.anterior = None
    lista = inserir(lista, aux.jogador)
    return lista

def remover_espec(lista, jogador):
    if lista is None:
        print("Sem jogadores na fila")
        return None
    aux = lista
    anterior = None
    while aux is not None:
        if aux.jogador == jogador:
            if aux.anterior is None and aux.proximo is None:
                return None 
            elif aux.anterior is None:
                lista = aux.proximo
                lista.anterior = None
                return lista
            elif aux.proximo is None:
                aux.anterior.proximo = None
                return lista
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista
        anterior = aux
        aux = aux.proximo
    print("Jogador não encontrado.")
    return lista

def menu():
    print("\n==== MENU ====")
    print("1 - Inserir novo jogador")
    print("2 - Simular uma rodada")
    print("3 - Simular X rodadas")
    print("4 - Mostrar fila de jogadores")
    print("5 - Mostrar o próximo a jogar")
    print("6 - Limpar a Fila")
    print("7 - Remover jogador da fila")
    print("8 - Sair")
    opc = int(input("Digite a opção desejada: "))
    return opc

def main():
    lista = None
    opc = 0
    while opc != 8:
        opc = menu()
        if opc == 1:
            jogador = input("Digite o nome do jogador a ser inserido: ")
            lista = inserir(lista, jogador)
        elif opc == 2:
            lista = remover_padrao(lista)
        elif opc == 3:
            num = int(input("Digite a quantidade de rodadas a serem simuladas: "))
            for i in range(num):
                lista = remover_padrao(lista)
                listar(lista)
        elif opc == 4:
            listar(lista)
        elif opc == 5:
            if lista is None:
                print("Fila vazia.")
            else:
                print("Próximo a jogar:", lista.jogador)
        elif opc == 6:
            print("<> Fila Limpa <>")
            lista = None
        elif opc == 7:
            jogador = input("Digite o nome do jogador que abandonou a fila: ")
            lista = remover_espec(lista, jogador)
        elif opc == 8:
            print("Obrigado por jogar!")

main()