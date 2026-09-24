class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("Carro ligado!")

    def desligar(self):
        print("Carro desligado!")


def main():
    p1 = Pessoa("Ana", 30)
    p2 = Pessoa("Bruno", 25)
    p1.apresentar()
    p2.apresentar()

    r = Retangulo(5, 3)
    print("Área:", r.area())
    print("Perímetro:", r.perimetro())

    c = Carro("Fiat", "Uno", 2015)
    print(c.marca, c.modelo, c.ano)
    c.ligar()
    c.desligar()


main()
