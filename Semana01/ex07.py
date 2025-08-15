'''
Intercalar duas listas ordenadas: Dadas duas listas ordenadas,
crie uma função que retorne uma nova lista contendo os elementos de ambas,
também em ordem.
'''      
def lista_unida(array1, array2):
    array3 = []

    while array1 and array2:
        if array1[0] < array2[0]:
            array3.append(array1.pop(0))
        else:
            array3.append(array2.pop(0))

    array3.extend(array1)
    array3.extend(array2)

    return array3

def main():
    array = [1,3,6,7,9]
    array2 = [2,4,5,8,10]
    array3 = lista_unida(array, array2)
    print(array3)
    
main()