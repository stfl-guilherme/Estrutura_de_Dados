class NoDeploy:
    def __init__(self, nome, duracao, ambiente, ativo=False):
        self.nome = nome
        self.duracao = duracao
        self.ambiente = ambiente
        self.ativo = ativo
        self.proximo = None


ORDEM_AMBIENTE = {"teste": 0, "homologação": 1, "produção": 2}


def adicionar(lista, nome, duracao, ambiente, ativo=False):
    novo = NoDeploy(nome, duracao, ambiente, ativo)

    if lista == None:
        novo.proximo = novo
        lista = novo
        return lista

    aux = lista
    while aux.proximo != lista:
        aux = aux.proximo
    aux.proximo = novo
    novo.proximo = lista
    return lista


def listar_todos(lista):
    if lista == None:
        print("Nenhum deploy cadastrado")
        return

    deploys = []
    aux = lista
    while True:
        deploys.append(aux)
        aux = aux.proximo
        if aux == lista:
            break

    deploys.sort(key=lambda d: ORDEM_AMBIENTE.get(d.ambiente, 99))

    for d in deploys:
        estado = "ativo" if d.ativo else "inativo"
        print(d.ambiente, "|", d.nome, "|", d.duracao, "s |", estado)


def listar_ativos(lista):
    if lista == None:
        print("Nenhum deploy cadastrado")
        return

    aux = lista
    encontrou = False
    while True:
        if aux.ativo:
            print(aux.ambiente, "|", aux.nome, "|", aux.duracao, "s")
            encontrou = True
        aux = aux.proximo
        if aux == lista:
            break

    if not encontrou:
        print("Nenhum deploy ativo")


def tempo_total(lista):
    if lista == None:
        return 0

    soma = 0
    aux = lista
    while True:
        soma = soma + aux.duracao
        aux = aux.proximo
        if aux == lista:
            break

    return soma


def ativar(lista, nome):
    if lista == None:
        print("Nenhum deploy cadastrado")
        return

    aux = lista
    while True:
        if aux.nome == nome:
            aux.ativo = True
            return
        aux = aux.proximo
        if aux == lista:
            break

    print("Deploy não encontrado:", nome)


def desativar(lista, nome):
    if lista == None:
        print("Nenhum deploy cadastrado")
        return

    aux = lista
    while True:
        if aux.nome == nome:
            aux.ativo = False
            return
        aux = aux.proximo
        if aux == lista:
            break

    print("Deploy não encontrado:", nome)


def excluir(lista, nome):
    if lista == None:
        print("Nenhum deploy cadastrado")
        return lista

    aux = lista
    anterior = None

    while True:
        if aux.nome == nome:
            if aux.proximo == aux:  # único elemento da lista
                return None
            if aux == lista:  # é a cabeça; precisa achar o último pra religar
                ultimo = lista
                while ultimo.proximo != lista:
                    ultimo = ultimo.proximo
                lista = lista.proximo
                ultimo.proximo = lista
                return lista
            anterior.proximo = aux.proximo
            return lista
        anterior = aux
        aux = aux.proximo
        if aux == lista:
            print("Deploy não encontrado:", nome)
            return lista


def menu():
    print("\n1 - Adicionar deploy")
    print("2 - Listar todos (por ambiente)")
    print("3 - Listar apenas ativos")
    print("4 - Tempo total dos deploys")
    print("5 - Ativar um deploy")
    print("6 - Desativar um deploy")
    print("7 - Excluir um deploy")
    print("8 - Sair")
    opc = int(input("Digite a opção:"))
    return opc


def main():
    opcao = 0
    lista = None

    while opcao != 8:
        opcao = menu()
        if opcao == 1:
            nome = input("Nome do deploy:")
            duracao = int(input("Duração (segundos):"))
            ambiente = input("Ambiente (teste/homologação/produção):")
            lista = adicionar(lista, nome, duracao, ambiente)
        elif opcao == 2:
            listar_todos(lista)
        elif opcao == 3:
            listar_ativos(lista)
        elif opcao == 4:
            print("Tempo total:", tempo_total(lista), "segundos")
        elif opcao == 5:
            nome = input("Nome do deploy para ativar:")
            ativar(lista, nome)
        elif opcao == 6:
            nome = input("Nome do deploy para desativar:")
            desativar(lista, nome)
        elif opcao == 7:
            nome = input("Nome do deploy para excluir:")
            lista = excluir(lista, nome)


main()
