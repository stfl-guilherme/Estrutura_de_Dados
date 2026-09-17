class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None


def inserir(fila, nome):
    novo = No(nome)
    if fila is None:
        return novo
    aux = fila
    while aux.proximo is not None:
        aux = aux.proximo
    aux.proximo = novo
    novo.anterior = aux
    return fila


def contar(fila):
    aux = fila
    contador = 0
    while aux is not None:
        contador += 1
        aux = aux.proximo
    return contador


def excluir(fila):
    if fila is None:
        print("Nenhum chamado na fila.")
        return None
    removido = fila
    fila = fila.proximo
    if fila is not None:
        fila.anterior = None
    print("Atendido:", removido.nome)
    return fila


def mostrar_status(fila):
    total = contar(fila)
    print("Chamados aguardando:", total)
    if fila is None:
        print("Próximo: nenhum")
    else:
        print("Próximo:", fila.nome)


def main():
    fila = None
    while True:
        print("\n--- Suporte de TI ---")
        print("1 - Registrar novo chamado")
        print("2 - Atender chamado (remove o primeiro da fila)")
        print("3 - Mostrar quantos aguardam e quem é o próximo")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da pessoa: ")
            fila = inserir(fila, nome)
        elif opcao == "2":
            fila = excluir(fila)
        elif opcao == "3":
            mostrar_status(fila)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
