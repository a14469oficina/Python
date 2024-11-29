import random

class NaveModelo:
    def __init__(self, denominacao, cor, perda_energia, letra):
        self.denominacao = denominacao
        self.cor = cor
        self.energia = 100  # Energia inicial
        self.perda_energia = perda_energia
        self.letra = letra

    def perder_energia(self):
        self.energia -= self.perda_energia
        if self.energia < 0:
            self.energia = 0
        return self.energia

class NaveComEnergiaExtra(NaveModelo):
    def __init__(self, denominacao, cor, perda_energia, letra, energia_extra):
        super().__init__(denominacao, cor, perda_energia, letra)
        self.energia_extra = energia_extra

    def mostrar_dados(self):
        print(f"Nave: {self.denominacao}, Energia: {self.energia}, Letra: {self.letra}")
        # Exibe o nome da nave com a cor associada
        print(f"\033[{self.cor}m{self.denominacao}\033[0m")

    def adicionar_energia_extra(self):
        self.energia += self.energia_extra
        if self.energia > 100:
            self.energia = 100
        return self.energia