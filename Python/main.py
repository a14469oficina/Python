import modules #importa todas as funções de outro ficheiro
#import modules as m # Faz o mesmo mas troca o nome
#from modules import mult , soma # Importa funções especificas do outro ficheiro
from sys import platform

boasvindas = "Ola Python"
print(modules.soma(4,5))
print(modules.mult(7,9))

platform = "Minha plataforma"
print(platform)