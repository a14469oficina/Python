from pessoas import Pessoa
import json

nome_do_ficheiro = "lista_pessoas.json"
pessoas = []

#print(__name__)
if __name__ == "__main__":
    for i in range(3):
        nome = input(f"Digite o nome da pessoa nº{i+1}: ")
        idade = int(input(f"Digite a idade da pessoa nº{i+1}: "))
        pessoas.append(Pessoa(nome,idade).__dict__)

    with open(nome_do_ficheiro, "w",encoding="utf8") as f:
        json.dump(pessoas,f,ensure_ascii= False,indent=2)

print("Dados guardados com sucesso!")
#print(*pessoas,sep="\n")