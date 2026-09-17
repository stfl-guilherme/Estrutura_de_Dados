class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


def empilhar(pilha, valor):
    novo = No(valor)
    if pilha is not None:
        novo.proximo = pilha
        pilha.anterior = novo
    return novo


def listar(pilha):
    if pilha is None:
        print("Histórico vazio.")
        return
    aux = pilha
    contador = 1
    while aux is not None:
        print(contador, "-", aux.valor)
        aux = aux.proximo
        contador += 1


def mostrar_topo(pilha):
    if pilha is None:
        print("Histórico vazio.")
        return
    print("Última ação registrada:", pilha.valor)


def desempilhar(pilha):
    if pilha is None:
        print("Histórico vazio.")
        return None
    removido = pilha
    pilha = pilha.proximo
    if pilha is not None:
        pilha.anterior = None
    print("Ação desfeita:", removido.valor)
    return pilha


def main():
    pilha = None
    while True:
        print("\n--- Histórico de Desfazer ---")
        print("1 - Registrar nova ação")
        print("2 - Desfazer última ação")
        print("3 - Mostrar histórico completo")
        print("4 - Mostrar última ação")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            acao = input("Descreva a ação: ")
            pilha = empilhar(pilha, acao)
        elif opcao == "2":
            pilha = desempilhar(pilha)
        elif opcao == "3":
            listar(pilha)
        elif opcao == "4":
            mostrar_topo(pilha)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
