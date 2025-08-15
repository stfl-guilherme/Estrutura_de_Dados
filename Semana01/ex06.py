'''
Maior subsequência crescente contínua: Dada uma lista de inteiros,
encontre a maior subsequência crescente e contínua dentro da lista.
'''
def maior_subsequencia_crescente(lista):
    if not lista:
        return []

    maior_sub = []        
    sub_atual = [lista[0]] 

    for i in range(1, len(lista)):
        if lista[i] > lista[i - 1]:
            
            sub_atual.append(lista[i])
        else:
           
            if len(sub_atual) > len(maior_sub):
                maior_sub = sub_atual
            
            sub_atual = [lista[i]]

    
    if len(sub_atual) > len(maior_sub):
        maior_sub = sub_atual

    return maior_sub

def main():
    lista = [2, 3, 1, 2, 3, 4, 1, 2]
    resultado = maior_subsequencia_crescente(lista)
    print("Maior subsequência crescente contínua:", resultado)

main()