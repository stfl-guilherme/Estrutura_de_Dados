'''
Crie uma classe Funcionario com os atributos: nome, salário e cargo.
Implemente um método calcular_bonus() que retorne:
10% de bônus para o cargo "Gerente"
5% de bônus para os demais cargos

Instancie dois funcionários e exiba o salário com bônus de cada um.
'''
class Funcionario:

    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_bonus(self):
        if self.cargo == "Gerente":
            self.salario *= 1.10
        else:
            self.salario *= 1.05
        return self.salario
    
    def __str__(self):
        return f"Salário de, {self.nome}, é de, {self.salario}, pois tem o cargo de ", {self.cargo}

jairo = Funcionario("Jairo", 1750, "Empregado")
adalberto = Funcionario("Adalberto", 2250, "Gerente")
jairo.calcular_bonus()
adalberto.calcular_bonus()
print(jairo.__str__())
print(adalberto.__str__())