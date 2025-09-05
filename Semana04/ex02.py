'''
Faça um algoritmo que utilize lista duplamente encadeada para armazenar informações de alunos. Cada nó deve conter:
Identificador (ID)
Nome do aluno
Nota final
O algoritmo deve apresentar o seguinte menu principal:
Inserir aluno
Listar alunos
Remover aluno
Mostrar situação dos alunos
Listar todos os alunos classificados como:
Aprovado (nota ≥ 7,0)
Exame (nota entre 4,0 e 6,9)
Reprovado (nota < 4,0)
Sair
'''
class No:
    def __init__(self, id, nome, nota_final):
        self.id = id
        self.nome = nome
        self.nota_final = nota_final
        self.proximo = None
        self.anterior = None

def cadastrar_aluno(lista, id, nome, nota_final):
    aux = No(id, nome, nota_final)
    if lista is None:
        return aux
    else:
        aux.proximo = lista
        lista.anterior = aux
        return aux

def listar_alunos(lista):
    if lista is None:
        print("\n-=-=-=-=-=-=-=-=-=-=")
        print("Sem alunos cadastrados!")
        print("-=-=-=-=-=-=-=-=-=-=")
        return
    aux = lista
    while aux is not None:
        print("\n-=-=-=-=-=-=-=-=-=-=")
        print("ID:", aux.id)
        print("Aluno:", aux.nome)
        print("Nota Final:", aux.nota_final)
        print("-=-=-=-=-=-=-=-=-=-=")
        aux = aux.proximo

def deletar_aluno(lista, id):
    aux = lista
    while aux is not None:
        if aux.id == id:
            if aux.anterior is None and aux.proximo is None:
                return None
            elif aux.anterior is None:
                aux.proximo.anterior = None
                return aux.proximo
            elif aux.proximo is None:
                aux.anterior.proximo = None
                return lista
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista
        aux = aux.proximo
    print("\n-=-=-=-=-=-=-=-=-=-=")
    print("Aluno não encontrado")
    print("-=-=-=-=-=-=-=-=-=-=")
    return lista

def situacao(lista):
    if lista is None:
        print("\n-=-=-=-=-=-=-=-=-=-=")
        print("Sem alunos cadastrados!")
        print("-=-=-=-=-=-=-=-=-=-=")
        return
    aux = lista
    while aux is not None:
        print("\n-=-=-=-=-=-=-=-=-=-=")
        print("ID:", aux.id)
        print("Aluno:", aux.nome)
        if aux.nota_final >= 7:
            print("Situação: APROVADO")
        elif 4 <= aux.nota_final <= 6.9:
            print("Situação: EXAME")
        else:
            print("Situação: REPROVADO")
        print("-=-=-=-=-=-=-=-=-=-=")
        aux = aux.proximo

def menu():
    print("\n-=-=-=-=-=-=-=-=-=-=")
    print("<1> Cadastrar aluno")
    print("<2> Listar alunos")
    print("<3> Remover aluno")
    print("<4> Situação dos alunos")
    print("<5> Sair")
    print("-=-=-=-=-=-=-=-=-=-=\n")
    opc = int(input("Digite o número da opção desejada: "))
    return opc

def main():
    lista = None
    opc = 0
    while opc != 5:
        opc = menu()
        if opc == 1:
            nome = input("\nDigite o nome do aluno: ")
            id = int(input("Digite o ID do aluno: "))
            nota_final = float(input("Digite a nota final do aluno: "))
            if nota_final > 10:
                nota_final = 10
            lista = cadastrar_aluno(lista, id, nome, nota_final)
        elif opc == 2:
            listar_alunos(lista)
        elif opc == 3:
            id = int(input("\nDigite o ID do aluno para remover: "))
            lista = deletar_aluno(lista, id)
        elif opc == 4:
            situacao(lista)
        elif opc == 5:
            print("Obrigado!")

main()