class No:
    def __init__(self, nome, emergencia):
        self.nome = nome
        self.emergencia = emergencia
        self.proximo = None
        self.anterior = None

def inserir(lista, nome, emergencia):
    novaVia = No(nome, emergencia)

    if lista == None:
        lista = novaVia
        lista.proximo = novaVia
        lista.anterior = novaVia
        return lista
    else:
        ultimo = lista.anterior
        novaVia.proximo = lista
        novaVia.anterior = ultimo
        ultimo.proximo = novaVia
        lista.anterior = novaVia
        return novaVia

def excluir(lista, nome):
    aux = lista

    while True:
        if aux.nome == nome:
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
            print("Elemento não encontrado")
            return lista

def listar(lista):
    aux = lista

    if lista == None:
        print("Lista vazia")
        return

    while True:
        print(aux.anterior.nome, "->", aux.nome, "->", aux.proximo.nome, "- emergencia:", aux.emergencia)
        aux = aux.proximo
        if aux == lista:
            return

def procuraremergencia(lista):
    aux = lista

    if lista == None:
        return None

    while True:
        if aux.emergencia == True:
            return aux
        aux = aux.proximo
        if aux == lista:
            return None

def simularciclo(lista, atual, passos):
    for i in range(passos):
        if lista == None:
            return atual

        viaEmergencia = procurarEmergencia(lista)
        if viaEmergencia != None:
            viaEmergencia.emergencia = False
            atual = viaEmergencia
            print(f"Passo {i + 1} (EMERGENCIA): abrindo {atual.nome}")
        else:
            print(f"Passo {i + 1}: abrindo {atual.nome}")

        atual = atual.proximo

    return atual

def menu():
    print("1 - Inserir via")
    print("2 - Excluir via")
    print("3 - Listar vias")
    print("4 - Marcar emergência")
    print("5 - Simular ciclo")
    print("6 - Sair")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    lista = None
    atual = None
    opcao = 0

    while opcao != 6:
        opcao = menu()
        if opcao == 1:
            nome = input("Nome da via:")
            lista = inserir(lista, nome, False)
            if atual == None:
                atual = lista
        elif opcao == 2:
            nome = input("Nome da via para excluir:")
            if atual != None and atual.nome == nome:
                atual = None
            lista = excluir(lista, nome)
            if atual == None:
                atual = lista
        elif opcao == 3:
            listar(lista)
        elif opcao == 4:
            nome = input("Nome da via em emergência:")
            aux = lista
            if lista != None:
                while True:
                    if aux.nome == nome:
                        aux.emergencia = True
                        break
                    aux = aux.proximo
                    if aux == lista:
                        print("Via não encontrada")
                        break
        elif opcao == 5:
            passos = int(input("Quantos passos simular:"))
            atual = simularCiclo(lista, atual, passos)

main()
