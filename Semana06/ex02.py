'''
Um ônibus urbano segue sempre o mesmo trajeto circular.
Cada nó da lista representa uma parada de ônibus.
Implemente funções para adicionar uma nova parada, remover uma parada e simular o percurso, imprimindo as paradas em sequência.
'''
class No:
    def __init__(self, nome_parada):
        self.nome_parada = nome_parada
        self.proximo = None
        self.anterior = None

def menu():
    print("-=-MENU-=-")
    print("1 - Adicionar parada")
    print("2 - Remover parada")
    print("3 - Simular percurso")
    print("4 - Sair")
    opc = int(input("Digite a opção: "))
    return opc

def adicionar_parada(lista, nome_parada):
    aux = No(nome_parada)
    if lista is None:
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
    
def remover_parada(lista, nome_parada):
    if lista is None:
        print("A lista está vazia!")
        return None

    aux = lista
    while True:
        if aux.nome_parada == nome_parada:
            # caso único nó
            if aux.proximo == aux:
                return None
            # removendo a cabeça
            elif aux == lista:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return aux.proximo
            # removendo outro nó qualquer
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista
        aux = aux.proximo
        if aux == lista:  
            print("Parada não encontrada!")
            return lista
        
def simular(lista):
    aux = lista
    if lista == None:
        print("A lista está vazia")
        return
    while True:
        print("Ultima Parada",aux.anterior.nome_parada ,"Parada Atual", aux.nome_parada,"Proxima Parada: ", aux.proximo.nome_parada)
        aux = aux.proximo
        if aux == lista:
            return lista
        
def main():
    opc = 0
    lista = None
    while opc != 4:
        opc = menu()
        if opc == 1:
            nome = input("Digite o nome da parada:\n")
            lista = adicionar_parada(lista, nome)
        elif opc == 2:
            nome = input("Digite o nome da parada para remover:\n")
            lista = remover_parada(lista, nome)
        elif opc == 3:
            lista = simular(lista)
        elif opc == 4:
            print("obrigado")
main()