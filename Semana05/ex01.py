'''
Crie uma classe Pessoa com atributos nome e idade. Implemente um método apresentar() que imprima uma mensagem com o nome e a idade da pessoa.
Crie dois objetos da classe Pessoa e chame o método apresentar() para cada um.
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.proximo = None

def menu():
    print("1 - adicionar pessoa")
    print("2 - apresentar pessoas")
    print("3 - sair")
    opc = int(input("Selecione a opção:"))
    return opc

def adicionar(lista, nome, idade):
    novo = Pessoa(nome, idade)
    if novo == None:
        return novo
    novo.proximo = lista
    return novo

def apresentar(lista):
    aux = lista
    if aux == None:
        print("Sem pessoas cadastradas!")
        return
    while aux != None:
        print(" -",aux.nome,aux.idade,"anos")
        aux = aux.proximo

def main():
    lista = None
    opc = 0
    while opc != 3:
        opc = menu()
        if opc == 1:
            people = input("Digite o nome da pessoa: ")
            idade = int(input("Digite a idade: "))
            lista = adicionar(lista, people, idade)
        elif opc == 2:
            apresentar(lista)
        elif opc == 3:
            print("Saindo...")
            
        else:
            print("opção inválida")

main()