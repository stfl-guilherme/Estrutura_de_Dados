class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


def inserir(fila, valor):
    novo = No(valor)
    if fila is None:
        return novo
    aux = fila
    while aux.proximo is not None:
        aux = aux.proximo
    aux.proximo = novo
    novo.anterior = aux
    return fila


def listar(fila):
    if fila is None:
        print("Nenhum carro na fila.")
        return
    aux = fila
    contador = 1
    while aux is not None:
        print(contador, "-", aux.valor)
        aux = aux.proximo
        contador += 1


def mostrar_proximo(fila):
    if fila is None:
        print("Nenhum carro na fila.")
        return
    print("Próximo carro a passar:", fila.valor)


def excluir(fila):
    if fila is None:
        print("Nenhum carro na fila.")
        return None
    removido = fila
    fila = fila.proximo
    if fila is not None:
        fila.anterior = None
    print("Passou pela cabine:", removido.valor)
    return fila


def main():
    fila = None
    while True:
        print("\n--- Fila do Pedágio ---")
        print("1 - Carro entra na fila")
        print("2 - Carro passa pela cabine")
        print("3 - Mostrar fila atual")
        print("4 - Mostrar próximo carro")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Placa do carro: ")
            fila = inserir(fila, placa)
        elif opcao == "2":
            fila = excluir(fila)
        elif opcao == "3":
            listar(fila)
        elif opcao == "4":
            mostrar_proximo(fila)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
