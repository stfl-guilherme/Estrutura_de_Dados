import random

class Sat:
    def __init__(self, id, altitude):
        self.id = id
        self.altitude = altitude
        self.integridade = 100
        self.proximo = None
        self.anterior = None

def menu():
    print("1 - cadastrar")
    print("2 - simular")
    print("3 - listar")
    print("4 - sair")
    opc = int(input("Digite o nº da opção: "))
    return opc

def cadastrar(lista, id ,altitude):
    aux = Sat(id, altitude)
    if lista == None:
        return aux
    else:
        aux.proximo = lista
        lista.anterior = aux   # ✅ corrigido
        return aux
    
def listar(lista):
    aux = lista
    if lista == None:
        print("Sem Satélites")
        return
    while aux != None:
        print("Satélite:", aux.id ,"altitude:", aux.altitude,"integridade:", aux.integridade)
        aux = aux.proximo
    
def simulacao(lista):
    if lista is None:
        print("Sem satélites")
        return lista

    # Conta quantos satélites existem
    aux = lista
    satelites = []
    while aux is not None:
        satelites.append(aux)
        aux = aux.proximo

    if len(satelites) < 2:
        print("Poucos satélites para colisão")
        return lista

    # Escolhe 2 diferentes
    s1, s2 = random.sample(satelites, 2)
    print(f"💥 Colisão entre {s1.id} e {s2.id}")
    s1.integridade -= 20
    s2.integridade -= 20

    return lista

def remover(lista):
    aux = lista
    if lista == None:
        print("Lista Vazia")
        return None

    while aux is not None:
        if aux.integridade <= 0:   # ✅ corrigido
            print(f"Removendo satélite {aux.id}")
            if aux.anterior is None and aux.proximo is None:   # só 1 satélite
                return None
            elif aux.anterior is None:  # primeiro nó
                aux.proximo.anterior = None
                return aux.proximo
            elif aux.proximo is None:   # último nó
                aux.anterior.proximo = None
                return lista
            else:                       # nó no meio
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista
        aux = aux.proximo
    return lista

def main():
    lista = None
    opc = 0
    while opc != 4:
        opc = menu()
        if opc == 1:
            nome = input("Digite o nome do satélite: ")
            altitude = int(input("Digite a altitude: "))
            lista = cadastrar(lista, nome, altitude)
        elif opc == 2:
            lista = simulacao(lista)
            lista = remover(lista)
        elif opc == 3:
            listar(lista)
        elif opc == 4:
            print("Encerrando...")
        else:
            print("Opção inválida")

main()