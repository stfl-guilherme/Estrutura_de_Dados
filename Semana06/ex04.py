'''
Em uma pizzaria, os clientes estão sentados em círculo e a pizza passa de mão em mão.
Cada nó representa um cliente.
Implemente a função para adicionar um cliente ao rodízio e outra para retirar um cliente que já foi embora.
Simule a passagem da pizza de pessoa em pessoa, imprimindo quem está recebendo a fatia.
'''
class No:
    def __init__(self, cliente):
        self.cliente = cliente
        self.proximo = None
        self.anterior = None


def adicionar_cliente(lista, cliente):
    aux = No(cliente)
    if lista is None:  # se a lista estiver vazia
        aux.proximo = aux
        aux.anterior = aux
        return aux
    else:  # insere no final
        ultimo = lista.anterior
        aux.proximo = lista
        aux.anterior = ultimo
        ultimo.proximo = aux
        lista.anterior = aux
        return lista


def retirar_cliente(lista, cliente):
    if lista is None:
        print("Nenhum cliente no rodízio.")
        return None

    aux = lista
    while True:
        if aux.cliente == cliente:
            # caso só tenha um cliente
            if aux.proximo == aux:
                return None
            # se for o primeiro
            elif aux == lista:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return aux.proximo
            # se for outro
            else:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return lista
        aux = aux.proximo
        if aux == lista:
            print("Cliente não encontrado.")
            return lista


def passar_pizza(lista, rodadas):
    if lista is None:
        print("Não há clientes para passar a pizza.")
        return
    aux = lista
    for i in range(rodadas):
        print(f"Rodada {i+1}: 🍕 entregue para {aux.cliente}")
        aux = aux.proximo


def menu():
    print("\n=== MENU PIZZARIA ===")
    print("1 - Adicionar cliente")
    print("2 - Remover cliente")
    print("3 - Passar pizza")
    print("4 - Sair")
    return int(input("Escolha: "))


def main():
    lista = None
    opc = 0
    while opc != 4:
        opc = menu()
        if opc == 1:
            nome = input("Digite o nome do cliente: ")
            lista = adicionar_cliente(lista, nome)
        elif opc == 2:
            nome = input("Digite o nome do cliente para remover: ")
            lista = retirar_cliente(lista, nome)
        elif opc == 3:
            rodadas = int(input("Quantas rodadas de pizza deseja simular? "))
            passar_pizza(lista, rodadas)
        elif opc == 4:
            print("Encerrando... Obrigado pela visita 🍕")
        else:
            print("Opção inválida!")


main()