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
        print("Pilha vazia.")
        return
    aux = pilha
    contador = 1
    while aux is not None:
        print(contador, "-", aux.valor)
        aux = aux.proximo
        contador += 1


def mostrar_topo(pilha):
    if pilha is None:
        print("Pilha vazia.")
        return
    print("Prato do topo:", pilha.valor)


def desempilhar(pilha):
    if pilha is None:
        print("Pilha vazia.")
        return None
    removido = pilha
    pilha = pilha.proximo
    if pilha is not None:
        pilha.anterior = None
    print("Retirado:", removido.valor)
    return pilha


def main():
    pilha = None
    while True:
        print("\n--- Pilha de Pratos ---")
        print("1 - Colocar prato na pilha")
        print("2 - Retirar prato do topo")
        print("3 - Mostrar pilha atual")
        print("4 - Mostrar prato do topo")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            prato = input("Tipo do prato: ")
            pilha = empilhar(pilha, prato)
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
