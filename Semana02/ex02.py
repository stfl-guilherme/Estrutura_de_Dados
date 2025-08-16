'''
Crie uma classe chamada Contato que armazene as seguintes informações: nome, telefone e e-mail.
Em seguida, instancie três objetos da classe e armazene-os em uma lista chamada agenda.
Por fim, percorra a lista e exiba o nome e o telefone de cada contato.
'''
class Contato:

    def __init__(self, nome, telefone, gmail):
        self.nome = nome
        self.telefone = telefone
        self.gmail = gmail

joao = Contato("João", 559964342, "joao@gmaiul.com.br")
mario = Contato("Mario", 5532890965, "quemario@gmaiul.com.br")
jonas = Contato("Jonas", 5509237434, "joninha@gmaiul.com.br")
agenda = []
agenda.append(joao,mario,jonas)
for Contato in agenda:
    print(Contato.nome)
    print(Contato.telefone)
    print(Contato.gmail)
    print("=-=-=-=-=-=-=-=-=-=-")