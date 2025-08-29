'''
Faça um algoritmo que contenha uma lista encadeada onde é armazenado apenas um valor float.
O sistema deve apresentar o seguinte menu:
Inserir 
Listar itens
Remover itens:
'''
class Floates:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
    
def menu():
    print("1. Inserir")
    print("2. Listar")
    print("3. remover")
    print("4. sair")
    opc = int(input("Digite o número da opção que você deseja: "))
    return opc

def inserir_item(lista,dado):
    novo =  Floates(dado)
    if novo == None:
        lista = novo
    else:
        novo.proximo = lista
    return novo

def listar_itens(lista):
    atual = lista
    if atual == None:
        print("lista vazia")
    else:
        while atual is not None:
            print("-", atual.dado)
            atual = atual.proximo

def deletar_item(lista, dado):
    atual = lista
    anterior = lista

    while atual is not None:
        if atual.dado == dado:
            if lista.proximo == None:
                print("Único atual da lista")
                return None
            elif atual == lista:
                print("Primeiro atual da lista")
                return atual.proximo
            elif atual.proximo == None:
                print("Ùltimo atual da lista")
                anterior.proximo = None
                return lista
            else:
                print("Elemento no meio da lista")
        anterior = atual
        atual = atual.proximo


def main():
    opcao = 0
    lista = None
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            dado = (float(input("Digite o float: ")))
            lista = inserir_item(lista, dado)
        elif opcao == 2:
            listar_itens(lista)
        elif opcao == 3:
            print("")
            listar_itens(lista)
            dado = (float(input("Digite o float para remover:")))
            lista = deletar_item(lista, dado)
        elif opcao == 4:
            print("Obrigado!")
        else:
            print("Opção Inválida!")

main()