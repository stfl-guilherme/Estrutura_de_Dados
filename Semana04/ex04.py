'''
Você foi contratado para desenvolver um pequeno sistema de gerenciamento de tarefas para uma agenda eletrônica.
Esse sistema deve ser capaz de:
Cadastrar uma nova tarefa no início da lista (inserção).
Remover uma tarefa com base na sua descrição (remoção).
Listar todas as tarefas na ordem em que foram cadastradas (listagem).
Cada tarefa deve conter:
Uma descrição (texto da tarefa, por exemplo: "Estudar para prova").
Um prazo (string ou data, como: "2025-08-10").
A estrutura de dados utilizada deve ser uma lista duplamente encadeada, com ponteiros para o anterior e o próximo elemento.
O sistema deve oferecer um menu simples em texto, com as opções:
Inserir nova tarefa
Remover tarefa existente
Listar todas as tarefas
Sair do programa
A função de remoção deve buscar a tarefa pela descrição (caso existam tarefas com a mesma descrição,
remova apenas a primeira encontrada).
O programa deve continuar executando até que o usuário escolha a opção de sair
'''
class Tarefa:
    def __init__(self, descricao, prazo):
        self.descricao = descricao
        self.prazo = prazo
        self.proximo = None
        self.anterior = None

def inserir_inicio(lista, descricao, prazo):
    nova = Tarefa(descricao, prazo)
    if lista is None:
        return nova
    else:
        nova.proximo = lista
        lista.anterior = nova
        return nova

def remover(lista, descricao):
    atual = lista
    while atual is not None:
        if atual.descricao == descricao:
            # caso único elemento
            if atual.anterior is None and atual.proximo is None:
                return None
            # caso seja o primeiro
            elif atual.anterior is None:
                atual.proximo.anterior = None
                return atual.proximo
            # caso seja o último
            elif atual.proximo is None:
                atual.anterior.proximo = None
                return lista
            # caso esteja no meio
            else:
                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                return lista
        atual = atual.proximo
    print("Tarefa não encontrada!")
    return lista

def listar(lista):
    if lista is None:
        print("\nNenhuma tarefa cadastrada!")
        return
    atual = lista
    print("\n--- Lista de Tarefas ---")
    while atual is not None:
        print(f"Descrição: {atual.descricao} | Prazo: {atual.prazo}")
        atual = atual.proximo
    print("-------------------------")

def menu():
    print("\n--- MENU ---")
    print("1. Inserir nova tarefa")
    print("2. Remover tarefa existente")
    print("3. Listar todas as tarefas")
    print("4. Sair")
    return int(input("Escolha: "))

def main():
    lista = None
    while True:
        opc = menu()
        if opc == 1:
            descricao = input("Digite a descrição da tarefa: ")
            prazo = input("Digite o prazo da tarefa (AAAA-MM-DD): ")
            lista = inserir_inicio(lista, descricao, prazo)
        elif opc == 2:
            descricao = input("Digite a descrição da tarefa a remover: ")
            lista = remover(lista, descricao)
        elif opc == 3:
            listar(lista)
        elif opc == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")

main()