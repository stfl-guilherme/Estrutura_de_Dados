'''
Um banco tem dois tipos de clientes: preferenciais e comuns.

Clientes comuns entram no final da fila.
Clientes preferenciais entram no início.
Quando um atendimento ocorre, o cliente do início da fila é atendido (removido).
O programa deve mostrar sempre a ordem atual de atendimento.
'''
class No:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo 
        self.proximo = None
        self.anterior = None

class FilaBanco:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def vazia(self):
        return self.inicio is None

    def adicionar_comum(self, nome):
        novo = No(nome, "Comum")
        if self.vazia():
            self.inicio = self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

    def adicionar_preferencial(self, nome):
        novo = No(nome, "Preferencial")
        if self.vazia():
            self.inicio = self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def atender(self):
        if self.vazia():
            print("Nenhum cliente na fila.")
        else:
            print("Atendendo:", self.inicio.nome, "-", self.inicio.tipo)
            self.inicio = self.inicio.proximo
            if self.inicio:
                self.inicio.anterior = None
            else:
                self.fim = None

    def mostrar_fila(self):
        if self.vazia():
            print("Fila vazia.")
        else:
            print("Fila de atendimento:")
            aux = self.inicio
            while aux:
                print(aux.nome, "-", aux.tipo)
                aux = aux.proximo


def menu():
    print("1 - Adicionar cliente comum")
    print("2 - Adicionar cliente preferencial")
    print("3 - Atender cliente")
    print("4 - Mostrar fila")
    print("5 - Sair")
    opc = int(input("Digite a opção desejada: "))
    return opc


def main():
    fila = FilaBanco()
    opc = 0
    while opc != 5:
        opc = menu()
        if opc == 1:
            nome = input("Digite o nome do cliente comum: ")
            fila.adicionar_comum(nome)
        elif opc == 2:
            nome = input("Digite o nome do cliente preferencial: ")
            fila.adicionar_preferencial(nome)
        elif opc == 3:
            fila.atender()
        elif opc == 4:
            fila.mostrar_fila()
        elif opc == 5:
            print("Encerrando o sistema.")

main()