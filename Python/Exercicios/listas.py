import os


ferramentas = ['Martelo','Alicate','Chave de fendas','Serra']

print(ferramentas[0])
ferramentas[2] = 'Parafusadeira'
# print(ferramentas[2])
# print(ferramentas)
# print(type(ferramentas))
#adicionar elemento no final da lista
ferramentas.append('Chave de fendas')
# print(ferramentas)
ferramentas.insert(1,'Furadeira')
# print(ferramentas)
# os.system("cls")
# for fr in ferramentas:
#     if fr.startswith(('C','P')):
#         print(f"x {fr}")

#remover o ultimo elemento da lsita
ferramentas.pop()
print(ferramentas)

#Remover um elem«nto especifico
ferramentas.pop(2)
print(ferramentas)

ferramentas.remove("Serra")
print(ferramentas)

del ferramentas[0]
print(ferramentas)

