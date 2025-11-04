'''
Adicione os seguintes métodos à sua árvore:
altura(no) – retorna a altura da árvore.
contar_nos(no) – retorna quantos nós há na árvore.
contar_folhas(no) – retorna quantas folhas há na árvore.
buscar(valor) – retorna True se o valor existir, ou False caso contrário.
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
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def em_ordem(self, no):
        if no:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    def pos_ordem(self, no):
        if no:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

    def altura(self, no):
        if no is None:
            return 0
        return 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def contar_nos(self, no):
        if no is None:
            return 0
        return 1 + self.contar_nos(no.esquerda) + self.contar_nos(no.direita)

    def contar_folhas(self, no):
        if no is None:
            return 0
        if no.esquerda is None and no.direita is None:
            return 1
        return self.contar_folhas(no.esquerda) + self.contar_folhas(no.direita)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        elif valor < no.valor:
            return self._buscar(no.esquerda, valor)
        else:
            return self._buscar(no.direita, valor)

def main():
    arvore = ArvoreBinaria()
    valores = [50, 30, 70, 20, 40, 60, 80]

    for v in valores:
        arvore.inserir(v)

    print("Pre-ordem:")
    arvore.pre_ordem(arvore.raiz)

    print("Em ordem:")
    arvore.em_ordem(arvore.raiz)

    print("Pos-ordem:")
    arvore.pos_ordem(arvore.raiz)

    print("Altura da árvore:", arvore.altura(arvore.raiz))
    print("Total de nós:", arvore.contar_nos(arvore.raiz))
    print("Total de folhas:", arvore.contar_folhas(arvore.raiz))

    valor_busca = 60
    print("Buscar valor", valor_busca, ":", arvore.buscar(valor_busca))

    valor_busca = 25
    print("Buscar valor", valor_busca, ":", arvore.buscar(valor_busca))

main()