'''
Leia um vetor de inteiros e mostre quantas vezes cada número aparece no vetor,
sem repetir a contagem para o mesmo valor.
'''

vetor = [1,9,2,1,5,3,2,1,6,4,3,9,5,6,7]
verificador = []

for i in range(len(vetor)):
    if vetor[i] not in verificador:
        verificador.append(vetor[i])
for j in range(len(verificador)):
    contador = 0
    for k in range(len(vetor)):
        if verificador[j] == vetor[k]:
            contador += 1
    texto = (f"O número {verificador[j]} aparece {contador} vezes!")
    verificador.pop(j)
    verificador.insert(j, texto)
for l in range(len(verificador)):
    print(verificador[l])