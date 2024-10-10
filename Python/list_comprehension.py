lista = []
lista_1 = [n for n in range(1,11)]
print(lista_1)

lista_2 = [n*2 for n in range(21)]
print(lista_2)

lista_3 = [
    num #elementos da lista
    for num in range(21)#elementos selecionados
    if num%2 == 0#filtro dos elementos
]
print(lista_3)

soma = sum ([n for n in range(11)])
print(soma)

from statistics import mean
media =mean([n for n in range(1,11)])
print(media)
