'''
Crie uma classe chamada Aluno que armazene as seguintes informações: nome do aluno e uma lista com três notas.
Em seguida, instancie três objetos da classe com nomes e notas diferentes e armazene-os em uma lista chamada turma.
Por fim, percorra a lista e exiba, para cada aluno, o nome e a média das três notas.
'''
class Aluno:
    def __init__(self, nome, *notas):
        self.nome = nome
        self.notas = list(notas)
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
a1 = Aluno("Marcio",6,4,3)
a2 = Aluno("Mario",3,10,9)
a3 = Aluno("Marcos", 8,4,6)
turma = [a1,a2,a3]
for aluno in turma:
    print("O Aluno", aluno.nome, "teve média de", aluno.calcular_media())