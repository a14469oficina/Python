# from colorama import Fore, Back # Back serve para trocar a cor do fundo da linha
# from getpass import getpass
# from random import randrange,randint

# print(Fore.LIGHTCYAN_EX + "Filipe" + Fore.RESET)
# getpass("Prima ENTER para continuar...")# o getpass serve para o programa esperar a interação(clicar em alguma tecla) do utilizador 
# print(Fore.LIGHTCYAN_EX + "Boas Pessoal" + Fore.RESET)


class Forma:
    def __init__(self,numLados,cor,) :
        self.numlados = numLados
        self.cor = cor

    def escrever(self):
        print(f"Métedo da classe Forma")

class Quadrado(Forma):
    def __init__(self, numLados, cor, diagonal):
        super().__init__(numLados, cor)
        self.diagonal = diagonal

    def escrever(self):
        print(f"Métedo da classe Quadrado")


q= Quadrado(4,"Azul",True)
q.escrever()
f= Forma(3,"Amarelo")
f.escrever()