class No:
    def __init__(self, id):
        self.id = id
        self.bastao = False
        self.proximo = None
        self.anterior = None

def adicionar_atleta(lista, id):
    aux = No(id)
    if lista == None:
        aux.bastao = True  # primeiro atleta começa com bastão
        lista = aux
        lista.proximo = aux
        lista.anterior = aux
        return lista
    else:
        ultimo = lista.anterior
        aux.proximo = lista
        aux.anterior = ultimo
        ultimo.proximo = aux 
        lista.anterior = aux
        return lista

def remover_atleta(lista, id):
    if lista is None:
        print("Lista vazia")
        return None

    aux = lista
    while True:
        if aux.id == id: 
            if aux.proximo == aux: 
                return None  # único atleta removido

            if aux.bastao:  
                # se quem saiu tinha o bastão, passa para o próximo
                aux.proximo.bastao = True

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                return aux.proximo
            else:
                return lista

        aux = aux.proximo
        if aux == lista:
            print("Atleta não encontrado")
            return lista

def simular_bastao(lista, voltas=10):
    if lista is None:
        print("Lista vazia")
        return None

    aux = lista
    for i in range(voltas):
        # encontra quem tem o bastão
        while not aux.bastao:
            aux = aux.proximo

        print(f"Turno {i+1}: Atleta {aux.id} está com o bastão")

        # passa o bastão
        aux.bastao = False
        aux.proximo.bastao = True
        aux = aux.proximo

    return lista

def menu():
    print("\n-=- MENU -=-")
    print("1 - Inserir")
    print("2 - Remover")
    print("3 - Simular")
    print("4 - Sair")
    opc = int(input("Digite a opção: "))
    return opc

def main():
    lista = None
    opc = 0

    while opc != 4:
        opc = menu()
        if opc == 1:
            id = int(input("Digite o ID do atleta: "))
            lista = adicionar_atleta(lista, id)
        elif opc == 2:
            id = int(input("Digite o ID do atleta para remover: "))
            lista = remover_atleta(lista, id)
        elif opc == 3:
            voltas = int(input("Quantos turnos deseja simular? "))
            lista = simular_bastao(lista, voltas)
        elif opc == 4:
            print("Obrigado")

main()
