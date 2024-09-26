notas_alunos = [
    ["Marcelo",12.5,17.8],
    ["Ana",13.25,14],
    ["Rui",17.25,9.25],
    ["Leonor",8.5,10.25]
]

for linha in range(4):
    for coluna in range(3):
        if coluna == 0:
            print(notas_alunos[linha][coluna], end=": ")
        elif coluna == 1:
            print(notas_alunos[linha][coluna], end=": ")
        else:
            print(notas_alunos[linha][coluna])

for c1,c2,c3 in notas_alunos:
    print(f"{c1}: {c2}, {c3}")

for linha in notas_alunos:
    print(f"{linha[0]}: {linha[1]}, {linha[2]}")