'''
implemente um algoritmo com lista duplamente encadeada para gerenciar uma playlist de músicas. Cada nó deve armazenar:
ID da música
Nome da música
Artista
Duração (em minutos)
O menu deve conter as seguintes opções:
Adicionar música na playlist
Listar todas as músicas
Remover música
Buscar música (por nome ou por artista)
Mostrar a duração total da playlist
Avançar para a próxima música / Voltar para a música anterior 
(usando os ponteiros da lista)
Sair
'''
class No:
    def __init__(self, id, nome, artista, duracao):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.proximo = None
        self.anterior = None

def inserir_musica(lista, id, nome, artista, duracao):
    aux = No(id, nome,  artista, duracao)
    if lista is None:
        return aux
    else:
        aux.proximo = lista
        lista.anterior = aux
        return aux

def listar_musicas(lista):
    if lista is None:
        print("\n-=-=-=-=-=-=-=-=-=-=")
        print("Sem Musicas na playlist!")
        print("-=-=-=-=-=-=-=-=-=-=")
        return
    aux = lista
    while aux is not None:
        print("\n-=-=-=-=-=-=-=-=-=-=")
        print("ID:", aux.id)
        print("Nome:", aux.nome)
        print("Artista:", aux.artista)
        print("Duração:", aux.duracao)
        print("-=-=-=-=-=-=-=-=-=-=")
        aux = aux.proximo

def remover_musica(lista, id):
    aux = lista
    while aux is not None:
        if aux.id == id:
            if aux.anterior is None and aux.proximo is None:
                return None
            elif aux.anterior is None:
                aux.proximo.anterior = None
                return aux.proximo
            elif aux.proximo is None:
                aux.anterior.proximo = None
                return lista
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista
        aux = aux.proximo
    print("\n-=-=-=-=-=-=-=-=-=-=")
    print("Musica Não Encontrada")
    print("-=-=-=-=-=-=-=-=-=-=")
    return lista

def buscar_musica_artista(lista, resp):
    aux = lista
    while aux is not None:
        if aux.artista == resp:
            print("Artista Encontrado")
            return
        else:
            aux = aux.proximo
    print("Artista não encontrado")

def buscar_musica_nome(lista, resp):
    aux = lista
    while aux is not None:
        if aux.nome == resp:
            print("Musica Encontrada")
            return
        else:
            aux = aux.proximo
    print("Musica não encontrada")

def contar_duracao(lista):
    aux = lista
    soma = 0
    while aux is not None:
        soma += aux.duracao
        aux = aux.proximo
    return soma

def menu():
    print("\n-=-=-=-=-=-=-=-=-=-=")
    print("<1> Adicionar Musica")
    print("<2> Listar Musicas")
    print("<3> Remover Musica")
    print("<4> Buscar Musica")
    print("<5> Mostrar Duração da Playlist")
    print("<6> Avançar/Voltar música")
    print("<7> Sair")
    print("-=-=-=-=-=-=-=-=-=-=\n")
    opc = int(input("Digite o número da opção desejada: "))
    return opc

def main():
    lista = None
    atual = None
    opc = 0
    while opc != 7:
        opc = menu()
        if opc == 1:
            nome = input("\nDigite o nome da musica: ")
            id = int(input("\nDigite o ID da musica: "))
            artista = input("\nDigite o nome do artista: ")
            duracao = int(input("\nDigite a duração da musica: "))
            lista = inserir_musica(lista, id, nome, artista, duracao)
            if atual is None:
                atual = lista
        elif opc == 2:
            listar_musicas(lista)
        elif opc == 3:
            id = int(input("\nDigite o ID da musica para remover: "))
            lista = remover_musica(lista, id)
        elif opc == 4:
            while True:
                print("Buscar por nome ou por artista")
                resp = input(": ").upper()
                if resp == "NOME":
                    resp = input("Digite o nome da musica: ")
                    buscar_musica_nome(lista, resp)
                    break
                if resp == "ARTISTA":
                    resp = input("Digite o nome do artista: ") 
                    buscar_musica_artista(lista, resp)
                    break
        elif opc == 5:
            contagem = contar_duracao(lista)
            print("A Duração da Playlist é")
            print(contagem,"minutos")
        elif opc == 6:
            if atual is None:
                print("Nenhuma música na playlist!")
                continue
            print("Tocando agora:", atual.nome)
            acao = input("Você quer ir para a próxima música ou voltar para a anterior? ").upper()
            if acao == "PROXIMA":
                if atual.proximo is not None:
                    atual = atual.proximo
                    print("Avançou para:", atual.nome)
                else:
                    print("Você já está na última música.")
            elif acao == "ANTERIOR":
                if atual.anterior is not None:
                    atual = atual.anterior
                    print("Voltou para:", atual.nome)
                else:
                    print("Você já está na primeira música.")
        elif opc == 7:
            print("Obrigado!")
        else:
            print("Opção inválida")

main()