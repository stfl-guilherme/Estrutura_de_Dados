'''
Desenvolva uma classe Retangulo com atributos largura e altura.
Adicione métodos para calcular a area() e o perimetro() do retângulo. Crie um objeto Retangulo e exiba seus cálculos.
'''
class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

def area(largura, altura):
    return largura * altura

def perimetro(largura, altura):
    return ((largura + altura) * 2)

print("-=-=-CALCULOS-=-=-")
print("<>Largura do Retangulo<>")
largura = float(input(""))
print("Salvando...")
print(">Aperte Enter para continuar<")
input("")
print("<>Altura do Retangulo<>")
altura = float(input(""))
print("Salvando...")
print(">Aperte Enter para continuar<")
input("")
print("Area do Retangulo = ", area(largura, altura))
print("Perimetro do Retangulo = ", perimetro(largura, altura))