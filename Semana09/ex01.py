'''
Implemente um programa que simule o funcionamento de operações matemáticas armazenadas em uma pilha. O menu deve conter as opções:

Inserir operação na pilha (ex: “5+3”, “7*2”)
Retirar última operação (POP)
Mostrar última operação inserida (topo)
Mostrar todas as operações pendentes
Sair
'''
class No:
    def __init__(self, conta):
        self.conta = conta
        self.proximo = None
        self.anterior = None


def push(top, conta):
    novo = No(conta)
    if top is None:
        return novo
    novo.anterior = top
    top.proximo = novo
    return novo


def pop(top):
    if top is None:
        print("A pilha está vazia!")
        return None
    print("Removendo operação:", top.conta)
    if top.anterior is None:
        return None  # se só tinha um elemento
    novo_topo = top.anterior
    novo_topo.proximo = None
    return novo_topo


def topo(top):
    if top is None:
        print("A pilha está vazia!")
    else:
        print("Última operação (topo):", top.conta)


def listar(top):
    if top is None:
        print("A pilha está vazia!")
        return
    print("\nOperações na pilha (do topo à base):")
    aux = top
    while aux is not None:
        print("-", aux.conta)
        aux = aux.anterior


def menu():
    print("\n-=- MENU PILHA -=-")
    print("1 - Inserir operação na pilha (PUSH)")
    print("2 - Retirar última operação (POP)")
    print("3 - Mostrar última operação (TOPO)")
    print("4 - Mostrar todas as operações")
    print("5 - Sair")
    opc = int(input("Digite a opção: "))
    return opc


def main():
    top = None
    opc = 0
    while opc != 5:
        opc = menu()
        if opc == 1:
            conta = input("Digite a operação (ex: 5+3): ")
            top = push(top, conta)
        elif opc == 2:
            top = pop(top)
        elif opc == 3:
            topo(top)
        elif opc == 4:
            listar(top)
        elif opc == 5:
            print("Encerrando o programa...")
        else:
            print("Opção inválida, tente novamente.")

main()