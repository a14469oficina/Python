# jogo.py

import os
import random
from Nave import NaveModelo, NaveComEnergiaExtra


    # Função para desenhar o tabuleiro 4x4
def desenhar_tabuleiro(tabuleiro):
    print("+----+---+---+---+")  # Borda superior
    for linha in tabuleiro:
        print("|", end=" ")  # Borda esquerda
        for cell in linha:
            print(f" {cell} ", end="|")  # Células do tabuleiro
        print("\n+----+---+---+---+")  # Linha de separação e borda direita
    print("\n")

# Função para inicializar o jogo (menu com título fancy)
def inicializar_jogo():
    os.system("cls")  # Limpar tela (no Linux/Unix, para Windows usar os.system('cls'))
    print("""
*******************************************                                                                                               
                                                                                                                                                                             
         ,---._      ,----..                   ,----..                                                                  ,--.                                                 
       .-- -.' \    /   /   \    ,----..      /   /   \              ,---,       ,---,       .--.--.                  ,--.'|   ,---,                       ,---,.   .--.--.    
       |    |   :  /   .     :  /   /   \    /   .     :           .'  .' `\    '  .' \     /  /    '.            ,--,:  : |  '  .' \             ,---.  ,'  .' |  /  /    '.  
       :    ;   | .   /   ;.  \|   :     :  .   /   ;.  \        ,---.'     \  /  ;    '.  |  :  /`. /         ,`--.'`|  ' : /  ;    '.          /__./|,---.'   | |  :  /`. /  
       :        |.   ;   /  ` ;.   |  ;. / .   ;   /  ` ;        |   |  .`\  |:  :       \ ;  |  |--`          |   :  :  | |:  :       \    ,---.;  ; ||   |   .' ;  |  |--`   
       |    :   :;   |  ; \ ; |.   ; /--`  ;   |  ; \ ; |        :   : |  '  |:  |   /\   \|  :  ;_            :   |   \ | ::  |   /\   \  /___/ \  | |:   :  |-, |  :  ;_     
       :         |   :  | ; | ';   | ;  __ |   :  | ; | '        |   ' '  ;  :|  :  ' ;.   :\  \    `.         |   : '  '; ||  :  ' ;.   : \   ;  \ ' |:   |  ;/|  \  \    `.  
       |    ;   |.   |  ' ' ' :|   : |.' .'.   |  ' ' ' :        '   | ;  .  ||  |  ;/  \   \`----.   \        '   ' ;.    ;|  |  ;/  \   \ \   \  \: ||   :   .'   `----.   \ 
   ___ l         '   ;  \; /  |.   | '_.' :'   ;  \; /  |        |   | :  |  ''  :  | \  \ ,'__ \  \  |        |   | | \   |'  :  | \  \ ,'  ;   \  ' .|   |  |-,   __ \  \  | 
 /    /\    J   : \   \  ',  / '   ; : \  | \   \  ',  /         '   : | /  ; |  |  '  '--' /  /`--'  /        '   : |  ; .'|  |  '  '--'     \   \   ''   :  ;/|  /  /`--'  / 
/  ../  `..-    ,  ;   :    /  '   | '/  .'  ;   :    /          |   | '` ,/  |  :  :      '--'.     /         |   | '`--'  |  :  :            \   `  ;|   |    \ '--'.     /  
\    \         ;    \   \ .'   |   :    /     \   \ .'           ;   :  .'    |  | ,'        `--'---'          '   : |      |  | ,'             :   \ ||   :   .'   `--'---'   
 \    \      ,'      `---`      \   \ .'       `---`             |   ,.'      `--''                            ;   |.'      `--''                '---" |   | ,'               
  "---....--'                    `---`                           '---'                                         '---'                                   `----'                 
                                                                                                                                                                                     
*******************************************
""")
    print("Pressione qualquer tecla para começar...")
    input()  # Aguardar uma tecla para começar

# Função principal para rodar o jogo
def jogo():
    # Inicializando naves
    nave1 = NaveComEnergiaExtra("Nave A", "31", 10, "A", 20)  # Cor 31 = Vermelho
    nave2 = NaveComEnergiaExtra("Nave B", "34", 15, "B", 15)  # Cor 34 = Azul
    nave3 = NaveComEnergiaExtra("Nave C", "32", 20, "C", 25)  # Cor 32 = Verde

    naves = [nave1, nave2, nave3]
    tiros_dados = 0
    tiros_certeiros = 0

    # Criando um tabuleiro vazio 4x4
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]

    # Posições aleatórias para as naves
    for nave in naves:
        while True:
            x, y = random.randint(0, 3), random.randint(0, 3)  # Tabuleiro 4x4
            if tabuleiro[x][y] == " ":
                tabuleiro[x][y] = nave.letra
                break

    # Exibindo o tabuleiro inicial
    os.system("cls")
    desenhar_tabuleiro(tabuleiro)
    
    # Começando o loop de tiros
    while tiros_dados < 105 and any(nave.energia > 0 for nave in naves):
        # Perguntando a posição dos tiros
        for _ in range(3):
            x_tiro, y_tiro = random.randint(0, 3), random.randint(0, 3)  # Tiros aleatórios no tabuleiro 4x4
            if tabuleiro[x_tiro][y_tiro] != " ":
                # Se o tiro acerta uma nave, perde energia
                for nave in naves:
                    if tabuleiro[x_tiro][y_tiro] == nave.letra:
                        nave.perder_energia()
                        tiros_certeiros += 1
                        break
                tabuleiro[x_tiro][y_tiro] = "X"  # Marca o tiro no tabuleiro
            tiros_dados += 1

        # Exibindo o tabuleiro após os tiros
        os.system("cls")
        desenhar_tabuleiro(tabuleiro)

        # Exibindo os dados das naves
        for nave in naves:
            if nave.energia > 0:
                nave.mostrar_dados()

        # Mostrando estatísticas
        eficacia = (tiros_certeiros / tiros_dados) * 100 if tiros_dados > 0 else 0
        print(f"\nTiros dados: {tiros_dados}, Tiros certeiros: {tiros_certeiros}, Eficácia: {eficacia:.2f}%")

        # Adicionando energia extra quando necessário
        if tiros_dados == 45:
            for nave in naves:
                if nave.energia > 0:
                    nave.adicionar_energia_extra()

        # Verificando se as naves foram aniquiladas
        if all(nave.energia == 0 for nave in naves):
            print("Todas as naves foram aniquiladas! Fim de jogo.")
            break

        # Pausa antes do próximo conjunto de tiros
        input("\nPressione uma tecla para continuar...")
        os.system("cls")  # Limpar a tela para o próximo round

    print("Jogo finalizado!")

# Função main para inicializar e chamar as funções do jogo
def main():
    inicializar_jogo()  # Exibe o menu inicial
    jogo()  # Inicia a execução do jogo

# Execução do programa
if __name__ == "__main__":
    main()