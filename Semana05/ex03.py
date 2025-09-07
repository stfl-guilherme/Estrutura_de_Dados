'''
Crie uma classe Carro com atributos marca, modelo e ano. Implemente um método ligar() que imprima "Carro ligado!" e um método desligar()
 que imprima "Carro desligado!". Crie um objeto Carro e demonstre o uso dos métodos.
'''
class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano

def menu():
    print("1 - Ligar o carro")
    print("2 - Desligar o carro")
    print("3 - Sair do carro")
    opc = int(input("Digite a opção"))
    return opc

def ligar(motor):
    motor = 1
    print("Seu carro ligado")
    return motor

def desligar(motor):
    motor = 0
    print("carro desligado")
    return motor
    
def main():
    motor = 0
    opc = 0
    marca = input("Digite a marca do seu carro:")
    modelo = input("Digite o modelo do seu carro:")
    ano = input("Digite o ano do seu carro:")
    meu_carro = Carro(marca,modelo,ano)

    while opc != 3:
        opc = menu()
        print("Seu carro", meu_carro.modelo,"da marca", meu_carro.marca, meu_carro.ano)
        if opc == 1:
            if motor == 1:
                print("O Carro já está ligado")
            else:
                motor = ligar(motor)
        elif opc == 2:
            if motor == 0:
                print("O Carro já está desligado!")
            else:
                motor = desligar(motor)
        elif opc == 3:
            print("Saindo")
main()