'''
Dado um vetor de números inteiros,
mova todos os elementos com valor zero para o final do vetor,
preservando a ordem dos demais elementos.
'''
vetor = [1,6,4,0,7,3,0,2,0]
for i in range(len(vetor)):
    if vetor[i] == 0:
        vetor.append(0)
        vetor.pop(i)
print(vetor)
