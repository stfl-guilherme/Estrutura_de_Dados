'''
Adicione os seguintes métodos à sua árvore:
minimo(no) → retorna o menor valor da árvore.
maximo(no) → retorna o maior valor da árvore.
media(no) → retorna a média dos valores
contar_maiores(no, limite) → conta quantos nós têm valor maior que o número informado
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

    def minimo(self, no):
        if no is None:
            return None
        while no.esquerda is not None:
            no = no.esquerda
        return no.valor

    def maximo(self, no):
        if no is None:
            return None
        while no.direita is not None:
            no = no.direita
        return no.valor

    def _soma_total(self, no):
        if no is None:
            return 0
        return no.valor + self._soma_total(no.esquerda) + self._soma_total(no.direita)

    def media(self, no):
        total_nos = self.contar_nos(no)
        if total_nos == 0:
            return 0
        soma = self._soma_total(no)
        return soma / total_nos

    def contar_maiores(self, no, limite):
        if no is None:
            return 0
        cont = 0
        if no.valor > limite:
            cont += 1
        cont += self.contar_maiores(no.esquerda, limite)
        cont += self.contar_maiores(no.direita, limite)
        return cont

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
    print("Menor valor:", arvore.minimo(arvore.raiz))
    print("Maior valor:", arvore.maximo(arvore.raiz))
    print("Média dos valores:", arvore.media(arvore.raiz))
    print("Nós maiores que 50:", arvore.contar_maiores(arvore.raiz, 50))

    valor_busca = 60
    print("Buscar valor", valor_busca, ":", arvore.buscar(valor_busca))

    valor_busca = 25
    print("Buscar valor", valor_busca, ":", arvore.buscar(valor_busca))

main()