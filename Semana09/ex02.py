'''
Os carros entram em uma garagem em fila indiana (um atrás do outro). Para um carro sair, 
é necessário retirar todos os que entraram depois dele (LIFO). Para isso, faça um algoritmo que já tenha cadastrado 20 carros. 
Depois peça para o usuário qual ele deseja tirar. 
Assim, você deverá tirar todos os outros que entraram na fila depois dele. Mostre todos os carros retirados.
'''
class No:
    def __init__(self, placa):
        self.placa = placa
        self.proximo = None
        self.anterior = None

def empilhar(top, placa):
    novo = No(placa)
    if top is None:
        return novo
    novo.anterior = top
    top.proximo = novo
    return novo

def listar(top):
    if top is None:
        print("Garagem vazia")
        return
    aux = top
    print("Carros na garagem:")
    while aux is not None:
        print(aux.placa)
        aux = aux.anterior

def retirar_carro(top, placa_busca):
    if top is None:
        print("Garagem vazia")
        return None

    aux = top
    carros_retirados = []

    while aux is not None:
        carros_retirados.append(aux.placa)
        if aux.placa == placa_busca:
            break
        aux = aux.anterior

    if aux is None:
        print("Carro não encontrado")
        return top

    print("Carros retirados:")
    for c in carros_retirados:
        print(c)

    novo_top = aux.anterior
    if novo_top is not None:
        novo_top.proximo = None
    else:
        novo_top = None

    return novo_top

def preencher_garagem():
    top = None
    for i in range(1, 21):
        placa = f"CARRO-{i:02d}"
        top = empilhar(top, placa)
    return top

def main():
    top = preencher_garagem()
    listar(top)
    print("Há 20 carros na garagem")
    placa = input("Digite a placa do carro que deseja retirar: ").upper()
    top = retirar_carro(top, placa)
    print("Garagem final:")
    listar(top)

main()