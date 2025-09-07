'''
Adicione à classe ListaDuplamenteEncadeada do exercício anterior um método percorrer_tras() que percorre a lista do fim ao início.
Teste a funcionalidade após adicionar alguns elementos.
'''
class No():
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

def inserir_dado(lista, dado):
    aux = No(dado)
    if lista == None:
        return aux
    else:
        aux.proximo = lista
        lista.anterior = aux
        return aux
    
def listar_dados(lista):
    aux = lista
    if aux == None:
        print("lista vazia")
        return
    while aux != None:
        print("- ",aux.dado)
        aux = aux.proximo

def lista_dados_inv(lista):
    aux = lista
    if aux == None:
        print("lista vazia")
        return
    while aux.proximo != None:
        aux = aux.proximo
    while aux is not None:
        print("- ",aux.dado)
        aux = aux.anterior

def menu():
    print("1 - inserir item")
    print("2 - listar itens")
    print("3 - lista dados na ordem invertida")
    opc = int(input("Digite a opção: "))
    return opc

def main():
    opc = 0
    lista = None
    while opc != 4:
        opc = menu()
        if opc == 1:
            dado = int(input("Digite o item para adionar: "))
            lista = inserir_dado(lista, dado)
        elif opc == 2:
            listar_dados(lista)    
        elif opc == 3:
            lista_dados_inv(lista) 
main()