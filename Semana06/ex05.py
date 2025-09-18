'''
Sistema de pacientes em triagem hospitalar 🏥
Cada paciente (nó) deve ter: nome, idade, prioridade (emergência, urgente, normal).
Funções obrigatórias:
Inserir paciente na fila.
Remover paciente atendido.
Mostrar todos os pacientes na ordem.
Simular o atendimento: percorra a lista circular e sempre atenda primeiro quem tem prioridade emergência, depois urgente e por último normal.
Sempre que o paciente é atendido, ele é retirado da lista
'''
class Paciente:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade  # "emergencia", "urgente", "normal"
        self.proximo = None
        self.anterior = None

def inserir_paciente(lista, nome, idade, prioridade):
    novo = Paciente(nome, idade, prioridade)
    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        return novo
    else:
        ultimo = lista.anterior
        novo.proximo = lista
        novo.anterior = ultimo
        ultimo.proximo = novo
        lista.anterior = novo
        return lista

def remover_paciente(lista, nome):
    if lista is None:
        print("Fila vazia.")
        return None
    aux = lista
    while True:
        if aux.nome == nome:
            if aux.proximo == aux:  # só 1 paciente
                return None
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                if aux == lista:
                    return aux.proximo
                else:
                    return lista
        aux = aux.proximo
        if aux == lista:
            print("Paciente não encontrado.")
            return lista

def mostrar_pacientes(lista):
    if lista is None:
        print("Nenhum paciente na fila.")
        return
    aux = lista
    print("\n--- Pacientes na fila ---")
    while True:
        print(f"{aux.nome} | Idade: {aux.idade} | Prioridade: {aux.prioridade}")
        aux = aux.proximo
        if aux == lista:
            break

def prioridade_valor(p):
    if p == "emergencia":
        return 3
    elif p == "urgente":
        return 2
    return 1  # normal

def simular_atendimento(lista):
    if lista is None:
        print("Nenhum paciente para atender.")
        return None
    
    atual = lista
    while lista is not None:
        # achar o paciente de maior prioridade
        aux = lista
        escolhido = aux
        while True:
            if prioridade_valor(aux.prioridade) > prioridade_valor(escolhido.prioridade):
                escolhido = aux
            aux = aux.proximo
            if aux == lista:
                break

        print(f"\nAtendendo paciente: {escolhido.nome} ({escolhido.prioridade})")
        lista = remover_paciente(lista, escolhido.nome)
    print("\nTodos os pacientes foram atendidos!")

def menu():
    print("\n--- Menu ---")
    print("1 - Inserir paciente")
    print("2 - Remover paciente")
    print("3 - Mostrar fila")
    print("4 - Simular atendimento")
    print("5 - Sair")
    return int(input("Escolha: "))

def main():
    lista = None
    while True:
        opc = menu()
        if opc == 1:
            nome = input("Nome do paciente: ")
            idade = int(input("Idade: "))
            prioridade = input("Prioridade (emergencia/urgente/normal): ").lower()
            lista = inserir_paciente(lista, nome, idade, prioridade)
        elif opc == 2:
            nome = input("Nome do paciente para remover: ")
            lista = remover_paciente(lista, nome)
        elif opc == 3:
            mostrar_pacientes(lista)
        elif opc == 4:
            lista = simular_atendimento(lista)
        elif opc == 5:
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")

main()