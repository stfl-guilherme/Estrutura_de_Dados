'''
Crie uma classe NoDuplo para uma lista duplamente encadeada, contendo dado, anterior e proximo.
Implemente uma classe ListaDuplamenteEncadeada com um método para adicionar um nó no início (adicionar_inicio)
e um método para percorrer a lista do início ao fim (percorrer_frente). Adicione elementos e demonstre o percurso.
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
        aux.anterior = aux
        return aux
    
def listar_dados(lista):
    aux = lista
    if aux == None:
        print("lista vazia")
        return
    while aux != None:
        print("- ",aux.dado)
        aux = aux.proximo

def menu():
    print("1 - inserir item")
    print("2 - listar itens")
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
main()