'''
Crie uma classe Livro com os atributos: título, autor e número de páginas.
Implemente um método que informe se o livro é "curto" ou "longo", considerando:
até 100 páginas = curto
mais de 100 páginas = longo

Crie dois objetos e mostre o resultado do método para cada um.
'''
class Livro:

    def __init__(self,titulo, autor, pag):
        self.titulo = titulo
        self.autor = autor
        self.pag = pag
        if pag <= 100:
            self.duracao = "curto"
        else:
            self.duracao = "longo"

    def __str__(self):
        return self.titulo,self.autor,self.pag,self.duracao

l1 = Livro("As mil visões de um cego", "Marquito", 127)
l2 = Livro("There is", "Paulo Cógus", 24)
print(l1.__str__())
print(l2.__str__())
