class NoServidor:
    def __init__(self, id_servidor, nome, status=False):
        self.id = id_servidor
        self.nome = nome
        self.status = status  # True = ligado, False = desligado
        self.anterior = None
        self.proximo = None


def inserir(lista_inicio, lista_fim, id_servidor, nome, status=False):
    novo = NoServidor(id_servidor, nome, status)

    if lista_inicio == None:
        lista_inicio = novo
        lista_fim = novo
        return lista_inicio, lista_fim

    lista_fim.proximo = novo
    novo.anterior = lista_fim
    lista_fim = novo
    return lista_inicio, lista_fim


def remover(lista_inicio, lista_fim, id_servidor):
    aux = lista_inicio

    if lista_inicio == None:
        print("Lista vazia")
        return lista_inicio, lista_fim

    while aux != None:
        if aux.id == id_servidor:
            if aux.anterior == None and aux.proximo == None:  # único elemento
                return None, None
            if aux.anterior == None:  # é o primeiro da lista
                lista_inicio = aux.proximo
                lista_inicio.anterior = None
                return lista_inicio, lista_fim
            if aux.proximo == None:  # é o último da lista
                lista_fim = aux.anterior
                lista_fim.proximo = None
                return lista_inicio, lista_fim
            # está no meio da lista
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            return lista_inicio, lista_fim
        aux = aux.proximo

    print("Servidor não encontrado:", id_servidor)
    return lista_inicio, lista_fim


def ligar(lista_inicio, id_servidor):
    aux = lista_inicio
    while aux != None:
        if aux.id == id_servidor:
            aux.status = True
            return
        aux = aux.proximo
    print("Servidor não encontrado:", id_servidor)


def desligar(lista_inicio, id_servidor):
    aux = lista_inicio
    while aux != None:
        if aux.id == id_servidor:
            aux.status = False
            return
        aux = aux.proximo
    print("Servidor não encontrado:", id_servidor)


def percorrer_frente(lista_inicio):
    aux = lista_inicio
    contador = 1

    if lista_inicio == None:
        print("Lista vazia")
        return

    while aux != None:
        estado = "ligado" if aux.status else "desligado"
        print(contador, "- ID:", aux.id, "| Nome:", aux.nome, "|", estado)
        aux = aux.proximo
        contador = contador + 1


def percorrer_tras(lista_fim):
    aux = lista_fim
    contador = 1

    if lista_fim == None:
        print("Lista vazia")
        return

    while aux != None:
        estado = "ligado" if aux.status else "desligado"
        print(contador, "- ID:", aux.id, "| Nome:", aux.nome, "|", estado)
        aux = aux.anterior
        contador = contador + 1


def main():
    inicio = None
    fim = None

    inicio, fim = inserir(inicio, fim, 1, "srv-web-01")
    inicio, fim = inserir(inicio, fim, 2, "srv-db-01")
    inicio, fim = inserir(inicio, fim, 3, "srv-cache-01")

    print("=== Servidores (frente) ===")
    percorrer_frente(inicio)

    ligar(inicio, 2)
    print("\n=== Após ligar o servidor 2 ===")
    percorrer_frente(inicio)

    desligar(inicio, 2)
    print("\n=== Após desligar o servidor 2 ===")
    percorrer_frente(inicio)

    inicio, fim = remover(inicio, fim, 1)
    print("\n=== Após remover o servidor 1 ===")
    percorrer_frente(inicio)

    print("\n=== Servidores (trás para frente) ===")
    percorrer_tras(fim)


main()
