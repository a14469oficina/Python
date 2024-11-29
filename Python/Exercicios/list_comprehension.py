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


produtos = [
    {"nome": "p1","preco": 10},
    {"nome": "p2","preco": 20},
    {"nome": "p3","preco": 30}
]

#Mapeamento
novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] >= 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep= "\n")

l = [1,2,3]
print(*l,sep= "\n")

nums = [4,7,11,3,12,21]

nova_lista = [
    num +1 if num > 10 else 0
    for num in nums
    if num > 11 #filter
]

print(*nova_lista)

lista = [
    
]


