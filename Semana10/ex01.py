'''
Implemente um programa em Python que simule um sistema de gerenciamento de chamados de TI utilizando um deque.
O sistema deve apresentar um menu interativo com as seguintes opções:

Adicionar chamado no fim da fila (chamado comum).
Adicionar chamado no início da fila (chamado urgente).
Atender chamado do início da fila (remoção do primeiro).
Atender chamado do fim da fila (remoção do último).
Listar todos os chamados da fila.
Sair do sistema.
'''
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def vazio(self):
        return self.inicio is None

    def adicionar_fim(self, dado):
        novo = No(dado)
        if self.vazio():
            self.inicio = self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

    def adicionar_inicio(self, dado):
        novo = No(dado)
        if self.vazio():
            self.inicio = self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def atender_inicio(self):
        if self.vazio():
            print("Fila vazia")
        else:
            print("Chamado atendido:", self.inicio.dado)
            self.inicio = self.inicio.proximo
            if self.inicio:
                self.inicio.anterior = None
            else:
                self.fim = None

    def atender_fim(self):
        if self.vazio():
            print("Fila vazia")
        else:
            print("Chamado atendido:", self.fim.dado)
            self.fim = self.fim.anterior
            if self.fim:
                self.fim.proximo = None
            else:
                self.inicio = None

    def listar(self):
        if self.vazio():
            print("Fila vazia")
        else:
            aux = self.inicio
            print("Chamados na fila:")
            while aux:
                print(aux.dado)
                aux = aux.proximo


def menu():
    print("1 - Adicionar chamado no fim (comum)")
    print("2 - Adicionar chamado no início (urgente)")
    print("3 - Atender chamado do início")
    print("4 - Atender chamado do fim")
    print("5 - Listar chamados")
    print("6 - Sair")
    opc = int(input("Digite a opção desejada: "))
    return opc

def main():
    fila = Deque()
    opc = 0
    while opc != 6:
        opc = menu()
        if opc == 1:
            chamado = input("Digite o nome do chamado comum: ")
            fila.adicionar_fim(chamado)
        elif opc == 2:
            chamado = input("Digite o nome do chamado urgente: ")
            fila.adicionar_inicio(chamado)
        elif opc == 3:
            fila.atender_inicio()
        elif opc == 4:
            fila.atender_fim()
        elif opc == 5:
            fila.listar()
        elif opc == 6:
            print("Encerrando o sistema")

main()