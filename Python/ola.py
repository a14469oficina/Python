# #print("privet blyat")

# '''
# print ("how are çãopai")
# '''

# x=8

# if x>7:
#     print("Conseguiu")
#     print("Parabens")
# elif x<3:
#     print("Chumbou")
# else:
#     print("Tentar de novo")

# x= "Filipe"
# n=16
# # print(x)
# # print(type(x))

# # print("O meu nome é", x,"e a minha idade é",n)
# # print("O meu nome é " + x + " e a minha idade é " + str(n))
# # print(f'O meu nome é {x} e a minha idade é {n}')


# produto1 = "Martelo"
# produto2 = "Alicate"
# produto3 = "Tesoura"

# print(produto1,end=', ')
# print(produto2,end=', ')
# print(produto3,)

# import os # Importa todas as funções do modulo
# from random import randrange # importa a função randrange do modulo random


# num1 = randrange(1,10)
# print(num1)
# num2 = randrange(1,20)
# print(num2)


# num1 = input("Digite o primeiro valor: ")
# num2 = input("Digite o segundo valor: ")
# print("Soma= ", int(num1)+int(num2))

# frase= "Maioria dos alunos"
# print(frase [0:12])#primeiros 11 caracteres
# print(frase [12:])
# print (len(frase))#total de caracteres^


frase= "Maioria das alunos"
frase2= frase.replace("Maioria","Minoria")
print(frase2)

lista_de_palavras = frase.split(" ")
print(type(lista_de_palavras))
print(lista_de_palavras)

for palavra in lista_de_palavras:
    print(palavra)

for i in range(10):
    print(i)