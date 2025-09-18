'''
Crie uma lista circular onde cada nó representa um atleta de um time.
Cada atleta possui um id e uma variável que representa se estão ou não com o bastão (True ou False)
Implemente funções para adicionar e remover atletas.
Faça uma simulação onde o bastão é passado de atleta para atleta (percorra a lista circular algumas vezes, mostrando quem tem o bastão em cada turno).
'''
class No:
    def __init__(self, id):
        self.id = id
        self.bastao = False
        self.proximo = None
        self.anterior = None

def adicionar_atleta(lista, id):
    aux = No(id)
    if lista == None:
        aux.bastao = True
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
        return aux

def remover_atleta(lista, id):
    aux = lista
    while True:
        if aux.id == id: 
            
            if aux.proximo == aux: 
                return None 

            elif aux == lista:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return lista.proximo
            
            elif aux.proximo == lista:
                aux.anterior.proximo = lista 
                aux.proximo.anterior = aux.anterior
                return lista 
            
            else:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return lista
        aux = aux.proximo
        if aux == lista:
            print("Atleta não encontrado")
            return  

def simular_bastao(lista):
    if lista is None:
        print("Lista vazia")
        return lista
    
    aux = lista
    while True: 
        if aux.bastao == True:
            print("\nAtleta -", aux.id)
            print("Com bastão\n")
            aux.bastao = False
            aux.proximo.bastao = True
            break
        aux = aux.proximo
        if aux == lista:
            break
    
    return lista

def menu():
    print("-=-MENU-=-")
    print("1- Inserir")
    print("2- Remover")
    print("3- Simular")
    print("4- Sair")
    opc = int(input("\nDigite a opção:\n"))
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
            lista = simular_bastao(lista)
        elif opc == 4:
            print("Obrigado")

main()