'''escreva uma função recursiva soma_impares(n) que calcule a soma de todos os números ímpares de 1 até n.'''

def impar(n):
    if n <= 0:
        return 1
    else:
        if n % 2 != 0:
            print(n)
            return n + impar(n - 1)
        return impar(n-1)
print(impar(9))