'''
Faça um algoritmo que possua uma lista duplamente encadeada e apresente o seguinte menu:
Inserir no
Listar no’s
Remover no’s
Verificar se no existe
Neste caso deve-se apresentar um novo menu e verificar se o usuário quer buscar por nome ou identificador.
Sair
Cada nó deve armazenar o nome e um identificador.
'''
class No:
    def __init__(self, nome, identificador):
        self.nome = nome
        self.identificador = identificador
        self.proximo = None
        self.anterior = None

def menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Inserir Nó")
    print("2 - Listar Nós")
    print("3 - Remover Nó")
    print("4 - Verificar Nó")
    print("5 - Sair")
    opc = int(input("Digite a opção desejada: "))
    return opc

def menu2():
    print("\n--- MENU DE BUSCA ---")
    print("1 - Buscar por nome")
    print("2 - Buscar por identificador")
    print("3 - Voltar")
    opc2 = int(input("Digite a opção desejada: "))
    return opc2

def inserir_item(lista, nome, identificador):
    novo = No(nome, identificador)
    if lista is None:
        return novo
    else:
        novo.proximo = lista
        lista.anterior = novo
        return novo   # novo vira a nova "cabeça" da lista

def listar_itens(lista):
    if lista is None:
        print("Lista vazia!")
        return
    aux = lista
    while aux is not None:
        print(f"- ID: {aux.identificador} | Nome: {aux.nome}")
        aux = aux.proximo

def deletar_item(lista, nome):
    aux = lista
    while aux is not None:
        if aux.nome == nome:
            # caso único nó
            if aux.anterior is None and aux.proximo is None:
                return None
            # caso seja o primeiro
            elif aux.anterior is None:
                aux.proximo.anterior = None
                return aux.proximo
            # caso seja o último
            elif aux.proximo is None:
                aux.anterior.proximo = None
                return lista
            # caso esteja no meio
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista
        aux = aux.proximo
    print("Nome não encontrado!")
    return lista

def verificar_no_identificador(lista, busca):
    aux = lista
    while aux is not None:
        if aux.identificador == busca:
            print(f"Item encontrado: ID={aux.identificador}, Nome={aux.nome}")
            return
        aux = aux.proximo
    print("Item não encontrado.")

def verificar_no_nome(lista, busca):
    aux = lista
    while aux is not None:
        if aux.nome == busca:
            print(f"Item encontrado: ID={aux.identificador}, Nome={aux.nome}")
            return
        aux = aux.proximo
    print("Item não encontrado.")

def main():
    lista = None
    opc = 0
    while opc != 5:
        opc = menu()
        if opc == 1:
            nome = input("Digite o nome para adicionar: ")
            identificador = int(input("Digite o ID para adicionar: "))
            lista = inserir_item(lista, nome, identificador)
        elif opc == 2:
            listar_itens(lista)
        elif opc == 3:
            nome = input("Digite o nome de um item para deletar: ")
            lista = deletar_item(lista, nome)
        elif opc == 4:
            opc2 = menu2()
            if opc2 == 1:
                nome = input("Digite o nome: ")
                verificar_no_nome(lista, nome)
            elif opc2 == 2:
                identificador = int(input("Digite o identificador: "))
                verificar_no_identificador(lista, identificador)
        elif opc == 5:
            print("Obrigado! Encerrando o programa...")

main()