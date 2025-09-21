class No:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais
        self.proximo = None
    
def percorrer(lista):
    if lista is None:
        print("Lista Vazia")
        return
    aux = lista
    while aux is not None:
        print("- Satélite:", aux.nome, "| País:", aux.pais)
        aux = aux.proximo

def remover(lista):
    if lista is None:
        print("Lista já está vazia")
        return None
    return lista.proximo 

def inserir(lista, nome, pais):
    aux = No(nome, pais) 
    if lista is None:
        return aux
    aux.proximo = lista
    return aux

def main():
    lista = None
    lista = inserir(lista, "Hubble", "Irlanda") 
    lista = inserir(lista, "James Web", "Paraguai")
    lista = inserir(lista, "Amazonia-1", "Brasil")
    print("\nLista de satélites:")
    percorrer(lista)
    lista = remover(lista)
    print("\nLista após remover o primeiro:")
    percorrer(lista)

main()