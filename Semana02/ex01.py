'''
Adicione à classe Produto um método chamado calcular_total() que retorna o valor total em estoque (preco * quantidade).
Depois, mostre o total de um produto.
'''
class Produto:

    def __init__(self, preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return (self.preco * self.quantidade)

arroz = Produto(2, 19)
print(arroz.calcular_total())