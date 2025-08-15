'''
Rotação de lista: Implemente uma função que rotacione os elementos de uma lista
 n posições à esquerda (ou à direita) -> usuário quem escolhe quantas posições 
e se é para direita ou esquerda.
'''
def rotacionar(vetor, n):
    n = n % len(vetor)
    return vetor[-n:] + vetor[:-n]

def perguntar():
    try:
        posicao = int(input("Digite quantas posições você deseja mover o elemento: "))
        direcao = input("Agora digite qual a direção (esquerda/direita): ").strip().lower()
        if direcao in ["direita", "d", "r", "right"]:
            return posicao
        elif direcao in ["esquerda", "e", "l", "left"]:
            return -posicao
        else:
            print("Direção inválida! Tente novamente.")
            return perguntar()
    except ValueError:
        print("Posição inválida! Digite um número inteiro.")
        return perguntar()

def main():
    vetor = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10]
    resultado = perguntar()
    vetor = rotacionar(vetor, resultado)
    print("Vetor rotacionado:", vetor)

main()