'''
Crie uma classe chamada Produto, que tenha os atributos: nome, preço e quantidade em estoque.
Implemente um método atualizar_estoque() que recebe um valor e soma à quantidade atual.
Crie dois objetos e atualize o estoque de cada um, mostrando os dados antes e depois da atualização.
'''
class Produto:

    def __init__(self,nome, preco, quantidade_est):
        self.nome = nome
        self.preco = preco
        self.quantidade_est = quantidade_est
    
    def __str__(self):
        return f"{self.nome}, {self.preco},{self.quantidade_est}"

    def atualizar_estoque(self, valor):
        self.quantidade_est += valor
        return self.nome,self.preco,self.quantidade_est

est1 = Produto("arroz", 17.99, 10)
est2 = Produto("carne", 27.99, 7)
valor = int(input("Digite a quantidade a ser adicionada: "))
valor2 = int(input("Digite a quantidade a ser adicionada: "))
print("Estoque antes: ", (str(est1))," Estoque Depois", est1.atualizar_estoque(valor))
print("Estoque antes: ", (str(est2))," Estoque Depois", est2.atualizar_estoque(valor2))