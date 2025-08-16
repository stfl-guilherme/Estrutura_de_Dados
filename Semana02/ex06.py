'''
Crie uma classe Aluno que receba nome e uma lista com três notas.
Implemente um método calcular_media() que retorne a média das notas.
Implemente também um método verificar_aprovacao(), que retorne "Aprovado" se a média for maior ou igual a 7, ou "Reprovado" caso contrário.
Teste a classe com dois alunos e mostre os resultados.
'''
class Aluno:

    def __init__(self, nome, *notas):
        '''
        if len(notas) != 3:
            raise ValueError("Você deve passar exatamente 3 notas.") limitar a 3 notas e enviar mensagem de erro
        '''
        self.nome = nome
        self.notas = list(notas)#vai receber infinitos valores se não limitar

    #def __init__(self, nome):
        #self.nome = nome
        #self.notas = []
#O que está em comentário seria a forma "arcaica"
    #def adicionar_nota(self, nota):
        #self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
   
    def verificar_aprovacao(self):
        if self.calcular_media() >= 7:
            return "aprovado"
        else: 
            return "reprovado"
        
aluno1 = Aluno("Roberto", 7,8,9)
aluno2 = Aluno("Junior", 4,2,3)
'''
aluno1 = Aluno("Roberto")
aluno1.adicionar_nota(7)
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(9)

aluno2 = Aluno("Junior")
aluno2.adicionar_nota(4)
aluno2.adicionar_nota(2)
aluno2.adicionar_nota(3)
'''
print("Média do ",aluno1.nome, "é", aluno1.calcular_media(),"e ele foi", aluno1.verificar_aprovacao())
print("Média do ",aluno2.nome, "é", aluno2.calcular_media(),"e ele foi", aluno2.verificar_aprovacao())