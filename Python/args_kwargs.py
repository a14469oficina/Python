aluno = {
    'nome': 'Joana Marques',
    'psi': 13.25,
    'port': 14.50,
    'mat': 11.33
}

def mediafinal(**valores):
    media = 0.0
    i = 0
    for disciplina, nota in valores.items():
        if isinstance(nota,float):
            print(f'{disciplina}: {nota} valores')
            media = media + nota
            i = i + 1
    media = media / i
    return media

m = mediafinal(**aluno)
print(m)

alunos = {
    'marcelo': {'nome': 'Marcelo Amorim', 'idade': 51},
    'ana': {'nome': 'Ana Abreu', 'idade': 53},
    'marta': {'nome': 'Marta Reis', 'idade': 19}
}

def maiorIdade(**als):
    mi = 0
    for al in als.values():
        if al['idade'] > mi:
            mi = al['idade']
    return mi

print(maiorIdade(**alunos))