'''
Implemente em Python uma árvore binária de busca (BST) com os seguintes métodos:
inserir(valor) – insere um novo nó na posição correta.
pre_ordem(no) – mostra os nós em pré-ordem.
em_ordem(no) – mostra os nós em ordem.
pos_ordem(no) – mostra os nós em pós-ordem.

Teste o programa inserindo os valores:
	50, 30, 70, 20, 40, 60, 80
'''
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir(no.direita, valor)

    def pre_ordem(self, no):
        if no:
            print(no.valor, end=' ')
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def em_ordem(self, no):
        if no:
            self.em_ordem(no.esquerda)
            print(no.valor, end=' ')
            self.em_ordem(no.direita)

    def pos_ordem(self, no):
        if no:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor, end=' ')

# --- Teste ---
arvore = ArvoreBinaria()
valores = [50, 30, 70, 20, 40, 60, 80]

for v in valores:
    arvore.inserir(v)

print("Pré-ordem:")
arvore.pre_ordem(arvore.raiz)
print("\nEm ordem:")
arvore.em_ordem(arvore.raiz)
print("\nPós-ordem:")
arvore.pos_ordem(arvore.raiz)