'''
Remoção de duplicatas mantendo a ordem: 
Crie uma função que remova elementos duplicados de uma lista, 
preservando a ordem em que os elementos aparecem pela primeira vez.
'''
def funcao(array):
    array_limpo = []

    for i in range(len(array)):
        if array[i] not in array_limpo:
            array_limpo.append(array[i])
    print(array_limpo)

def main():
    array = [0,1,2,3,3,4,2,4,1,4,2,9,6]
    funcao(array)
main()