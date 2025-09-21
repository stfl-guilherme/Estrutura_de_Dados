class Satellite:
    def __init__(self, nome, altitude, combustivel, ativo=True):
        if altitude < 300:
            raise ValueError("A altitude mínima permitida é 300 km.")
        if not (0 <= combustivel <= 100):
            raise ValueError("Combustível deve estar entre 0 e 100%.")
        
        self.nome = nome
        self.altitude = altitude
        self.combustivel = combustivel
        self.ativo = ativo
        self.next = None
        self.prev = None

class Orbita:
    def __init__(self):
        self.head = None

    # Adicionar satélite
    def adicionar_satellite(self, nome, altitude, combustivel):
        novo = Satellite(nome, altitude, combustivel)
        if self.head is None:
            self.head = novo
            novo.next = novo
            novo.prev = novo
        else:
            tail = self.head.prev
            tail.next = novo
            novo.prev = tail
            novo.next = self.head
            self.head.prev = novo
        print(f"Satélite {nome} adicionado em órbita.")

    # Remover satélite
    def remover_satellite(self, nome):
        if self.head is None:
            print("Nenhum satélite na órbita.")
            return
        
        atual = self.head
        while True:
            if atual.nome == nome:
                if atual.next == atual:  # Apenas 1 satélite
                    self.head = None
                else:
                    atual.prev.next = atual.next
                    atual.next.prev = atual.prev
                    if self.head == atual:
                        self.head = atual.next
                print(f"Satélite {nome} removido da órbita.")
                return
            atual = atual.next
            if atual == self.head:
                break
        print(f"Satélite {nome} não encontrado.")

    # Simulação de órbita
    def simular_orbita(self, consumo_por_volta=10):
        if self.head is None:
            print("Nenhum satélite para simular.")
            return
        
        atual = self.head
        to_remove = []
        while True:
            if atual.ativo:
                atual.combustivel -= consumo_por_volta
                if atual.combustivel <= 0:
                    atual.combustivel = 0
                    atual.ativo = False
                    print(f"Satélite {atual.nome} desativado (combustível esgotado).")
            atual = atual.next
            if atual == self.head:
                break
        
        # Remover satélites com combustível 0
        atual = self.head
        while atual and atual.ativo == False:
            next_sat = atual.next
            if atual.combustivel == 0:
                self.remover_satellite(atual.nome)
            atual = next_sat
            if atual == self.head:
                break

    # Percorrer sentido horário
    def percorrer_horario(self):
        if self.head is None:
            print("Nenhum satélite na órbita.")
            return
        atual = self.head
        print("Satélites em órbita (horário):")
        while True:
            print(f"{atual.nome} - Altitude: {atual.altitude} km - Combustível: {atual.combustivel}% - Ativo: {atual.ativo}")
            atual = atual.next
            if atual == self.head:
                break

    # Percorrer sentido anti-horário
    def percorrer_antihorario(self):
        if self.head is None:
            print("Nenhum satélite na órbita.")
            return
        atual = self.head.prev
        print("Satélites em órbita (anti-horário):")
        start = atual
        while True:
            print(f"{atual.nome} - Altitude: {atual.altitude} km - Combustível: {atual.combustivel}% - Ativo: {atual.ativo}")
            atual = atual.prev
            if atual == start:
                break

    # Reposicionar satélite
    def reposicionar_satellite(self, nome, nova_altitude):
        if nova_altitude < 300:
            print("Altitude mínima permitida é 300 km.")
            return
        atual = self.head
        while True:
            if atual.nome == nome:
                atual.altitude = nova_altitude
                print(f"Satélite {nome} reposicionado para {nova_altitude} km.")
                return
            atual = atual.next
            if atual == self.head:
                break
        print(f"Satélite {nome} não encontrado.")

    # Mostrar satélites ativados
    def mostrar_ativos(self):
        if self.head is None:
            print("Nenhum satélite na órbita.")
            return
        atual = self.head
        print("Satélites ativos:")
        while True:
            if atual.ativo:
                print(f"{atual.nome} - Altitude: {atual.altitude} km - Combustível: {atual.combustivel}%")
            atual = atual.next
            if atual == self.head:
                break

    # Mostrar satélites desativados
    def mostrar_desativados(self):
        if self.head is None:
            print("Nenhum satélite na órbita.")
            return
        atual = self.head
        print("Satélites desativados:")
        while True:
            if not atual.ativo:
                print(f"{atual.nome} - Altitude: {atual.altitude} km - Combustível: {atual.combustivel}%")
            atual = atual.next
            if atual == self.head:
                break


# Exemplo de uso
orbita = Orbita()
orbita.adicionar_satellite("Hubble", 540, 80)
orbita.adicionar_satellite("ISS", 408, 100)
orbita.adicionar_satellite("GPS IIF-5", 20180, 50)

orbita.percorrer_horario()
orbita.simular_orbita(consumo_por_volta=20)
orbita.percorrer_horario()
orbita.reposicionar_satellite("ISS", 420)
orbita.mostrar_ativos()
orbita.mostrar_desativados()