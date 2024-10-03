dados = [
    { 'nome': 'Marcelo', 'sexo': 'M', 'altura': 1.84, 'peso': 98 },
    { 'nome': 'Rui', 'sexo': 'M', 'altura': 1.94, 'peso': 83 },
    { 'nome': 'Joana', 'sexo': 'F', 'altura': 1.68, 'peso': 68 },
    { 'nome': 'Leonor', 'sexo': 'F', 'altura': 1.64, 'peso': 59 },
    { 'nome': 'Alfredo', 'sexo': 'M', 'altura': 1.87, 'peso': 105 }
]

lista_sexo = map(lambda pessoa: 1 if pessoa["sexo"] == "M" else 0 ,dados)
print(f"A lista numerica sobre sexo: {list(lista_sexo)}")