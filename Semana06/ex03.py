'''
🎯 Desafio: A Roleta Russa Circular

Em uma taverna sombria, um grupo de guerreiros participa de um jogo mortal: a Roleta
Russa Circular. Eles estão sentados em círculo e, a cada rodada, um guerreiro é
eliminado aleatoriamente. O processo continua até restar apenas um sobrevivente, que é declarado o vencedor.
Objetivo:
Crie uma lista duplamente encadeada circular que simule esse jogo.
A função deve aceitar uma quantidade inicial de guerreiros e exibir quem foi eliminado a cada rodada (utilize a função rand - levando em consideração o total de guerreiros).
Ao final, exiba o sobrevivente.
'''
import random

class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None


def criar_lista(guerreiros):
    lista = None
    for i in range(1, guerreiros + 1):
        lista = adicionar(lista, f"Guerreiro {i}")
    return lista


def adicionar(lista, nome):
    aux = No(nome)
    if lista is None:
        aux.proximo = aux
        aux.anterior = aux
        return aux
    else:
        ultimo = lista.anterior
        aux.proximo = lista
        aux.anterior = ultimo
        ultimo.proximo = aux
        lista.anterior = aux
        return lista


def eliminar(lista, escolhido):
    aux = lista
    while True:
        if aux.nome == escolhido:
            # caso único
            if aux.proximo == aux:
                return None, aux.nome
            # se for o primeiro
            elif aux == lista:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return aux.proximo, aux.nome
            # caso geral
            else:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return lista, aux.nome
        aux = aux.proximo


def roleta_russa(total):
    lista = criar_lista(total)

    while lista is not None and lista.proximo != lista:
        # contar quantos ainda restam
        vivos = []
        aux = lista
        while True:
            vivos.append(aux.nome)
            aux = aux.proximo
            if aux == lista:
                break

        escolhido = random.choice(vivos)
        lista, eliminado = eliminar(lista, escolhido)
        print(f"💀 {eliminado} foi eliminado!")

    print(f"\n🏆 O sobrevivente é: {lista.nome}")


# -------------------
# Executar o jogo
# -------------------
def main():
    guerreiros = int(input("Digite o número de guerreiros: "))
    roleta_russa(guerreiros)


main()