'''
Preencha um vetor com números inteiros e crie outro vetor contendo
apenas os números primos encontrados.
'''
vetor = [1,17,2,5,11,13,6,9]
vetor2 = []
for i in range(len(vetor)):
    contador = 0
    for j in range(1, vetor[i] + 1):
        if vetor[i] % j == 0:
            contador += 1
    if contador == 2:
        vetor2.append(vetor[i])

print(vetor2)