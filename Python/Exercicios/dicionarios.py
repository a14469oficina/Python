aluno = {
    "nome": "Russo",
    "nota_matematica": 18.3,
    "nota_portugues": 14,
    "outras_notas": [18.5,15.25,17,15.6]
}

print(aluno["outras_notas"][1])

for k in aluno: #imprime a chave
    print(k)
print("-------------------------")
for v in aluno.values(): #imprime os valores
    print(v)
print("-------------------------")
for k,v in aluno.items():
    print(f"{k}: {v}")

    

aluno = [

            {
                "nome": "Russo",
                "nota_matematica": 18.3,
                "nota_portugues": 14,
                "outras_notas": [18.5,15.25,17,15.6]
            },
            
            {
                "nome": "Lucas",
                "nota_matematica": 18,
                "nota_portugues": 17,
                "outras_notas": [17.5,16.25,14,16]
            }


]

print(aluno[1]["nome"])


nomes = ["marcelo","Filipe"]
print(nomes[0][2])

nome = "Marcelo"
nome =["M","a","r","c","e","l","o"]