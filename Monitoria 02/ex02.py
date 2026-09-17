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
        print("Fila de impressão vazia.")
        return
    aux = fila
    contador = 1
    while aux is not None:
        print(contador, "-", aux.valor)
        aux = aux.proximo
        contador += 1


def mostrar_proximo(fila):
    if fila is None:
        print("Fila de impressão vazia.")
        return
    print("Próximo documento a imprimir:", fila.valor)


def excluir(fila):
    if fila is None:
        print("Fila de impressão vazia.")
        return None
    removido = fila
    fila = fila.proximo
    if fila is not None:
        fila.anterior = None
    print("Impresso:", removido.valor)
    return fila


def main():
    fila = None
    while True:
        print("\n--- Fila de Impressão ---")
        print("1 - Enviar documento para impressão")
        print("2 - Imprimir próximo documento")
        print("3 - Mostrar fila de impressão")
        print("4 - Mostrar próximo documento")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            doc = input("Nome do documento: ")
            fila = inserir(fila, doc)
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
