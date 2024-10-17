# Crie uma lista com os números pares de 1 a 10.
lista = [
    n    
    for n in range (1,11)
    if n % 2 == 0
]
print(lista)


# 2. Crie uma lista com os quadrados dos números de 1 a 10.
nums = [1,2,3,4,5,6,7,8,9,10]
lista2 = [
    n*n   
    for n in nums
]
print(lista2)

# 3. Dada uma lista de palavras, crie uma nova lista que indique o tamanho de cada palavra.
palavras= ["Boas", "Saudade", "Gyat", "Comunismo"]
lista3 = [
    len(n)
    for n in palavras
]
print(lista3)
# 4. Dada uma lista de números, crie uma lista apenas com os números maiores que 5.
numeros = [7,4,9,71,12,4,5,6,43,2,77,58,99]
lista4 = [
    n if n > 5 else 0
    for n in numeros
    if n > 5
]
print(lista4)

# 5. Crie uma lista com as letras maiúsculas de uma string. (nome = 'MarcelO ViEiRa amorIM')
letras_maiusculas = "FilIPe ALEXandRe SobLiRoV"
lista5 = [
    n for n in letras_maiusculas if n.isupper()
]
print(lista5)

# 6. Dada uma lista de números, crie uma nova lista onde se o número for múltiplo de 3,
# é apresentado o dobro deste caso contrário aparece o mesmo número da lista original.

multiplo_3 = [3,6,9,12,15,2,7,8,4,5]
lista6 = [
    n*2 if n % 3 == 0 else n
    for n in multiplo_3
]
print(lista6)


# 7. Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam
# com a letra "A". Todos os nomes da nova lista devem aparecer em maiúsculas.


# 8. Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta,
# apenas para as frutas com mais de 5 letras. Caso contrário, deve aparecer 0.