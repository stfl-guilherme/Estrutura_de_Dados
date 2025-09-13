class Parada:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

def adicionar_parada(lista, nome):
    nova = Parada(nome)
    if lista is None:
        lista = nova
        lista.proximo = lista
        lista.anterior = lista
        return lista
    else:
        ultima = lista.anterior
        nova.proximo = lista
        nova.anterior = ultima
        ultima.proximo = nova
        lista.anterior = nova
        return lista  # head continua sendo o mesmo

def remover_parada(lista, nome):
    if lista is None:
        print("Não há paradas cadastradas.")
        return None

    aux = lista
    while True:
        if aux.nome == nome:
            if aux.proximo == aux:  
                return None  # só havia uma parada

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                return aux.proximo  # head muda para a próxima
            else:
                return lista

        aux = aux.proximo
        if aux == lista:
            print("Parada não encontrada.")
            return lista

def simular_percurso(lista, voltas=1):
    if lista is None:
        print("Nenhuma parada no trajeto.")
        return

    atual = lista
    for v in range(voltas):
        print(f"\nVolta {v+1}:")
        while True:
            print(f" Ônibus na parada: {atual.nome}")
            atual = atual.proximo
            if atual == lista:
                break

def mostrar_paradas(lista):
    if lista is None:
        print("Nenhuma parada cadastrada.")
        return
    atual = lista
    paradas = []
    while True:
        paradas.append(atual.nome)
        atual = atual.proximo
        if atual == lista:
            break
    print(" → ".join(paradas))

# ---------------- MAIN ----------------
def menu():
    print("\n-=- MENU -=-")
    print("1 - Adicionar parada")
    print("2 - Remover parada")
    print("3 - Mostrar paradas")
    print("4 - Simular percurso")
    print("5 - Sair")
    opc = int(input("Escolha: "))
    return opc

def main():
    lista = None
    while True:
        opc = menu()
        if opc == 1:
            nome = input("Digite o nome da parada: ")
            lista = adicionar_parada(lista, nome)
        elif opc == 2:
            nome = input("Digite o nome da parada para remover: ")
            lista = remover_parada(lista, nome)
        elif opc == 3:
            mostrar_paradas(lista)
        elif opc == 4:
            voltas = int(input("Quantas voltas o ônibus deve dar? "))
            simular_percurso(lista, voltas)
        elif opc == 5:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida.")

main()
