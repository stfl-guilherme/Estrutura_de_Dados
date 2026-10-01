class No:
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel
        self.proximo = None


def inserir_final(lista, nome, responsavel):
    novo = No(nome, responsavel)

    if lista == None:
        lista = novo
        return lista

    aux = lista
    while aux.proximo != None:
        aux = aux.proximo
    aux.proximo = novo
    return lista


def percorrer(lista):
    aux = lista
    contador = 1

    if lista == None:
        print("Lista vazia")
        return

    while aux != None:
        print(contador, "-", aux.nome, "| Responsável:", aux.responsavel)
        aux = aux.proximo
        contador = contador + 1


def remover(lista, nome):
    aux = lista
    anterior = None

    if lista == None:
        print("Lista vazia")
        return lista

    while aux != None:
        if aux.nome == nome:
            if aux == lista:  # é o primeiro nó da lista
                lista = lista.proximo
                return lista
            anterior.proximo = aux.proximo
            return lista
        anterior = aux
        aux = aux.proximo

    print("Sprint não encontrada:", nome)
    return lista


def main():
    sprints = None

    sprints = inserir_final(sprints, "Planejamento do Produto", "Ana")
    sprints = inserir_final(sprints, "Implementação do Backend", "João")
    sprints = inserir_final(sprints, "Testes Automatizados", "Carla")

    print("=== Sprints cadastradas ===")
    percorrer(sprints)

    sprints = remover(sprints, "Planejamento do Produto")

    print("\n=== Após remover 'Planejamento do Produto' ===")
    percorrer(sprints)


main()
