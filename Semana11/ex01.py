'''Crie uma função recursiva contagem_regressiva(n) que exiba os números de n até 1.'''

def somatorio(n):
    if n == 0:
        return
    print(n)
    return somatorio(n-1)

somatorio(9)