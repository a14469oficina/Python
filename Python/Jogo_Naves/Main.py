import os
from Jogo import inicializar_jogo, jogo  # Importa as funções do arquivo jogo.py

# Função main para inicializar e chamar as funções do jogo
def main():
    inicializar_jogo()  # Exibe o menu inicial com título e espera pela interação do jogador
    jogo()  # Inicia a execução do jogo, chama o loop de interações do jogo

# Execução do programa
if __name__ == "__main__":
    main()  # Chama a função main para iniciar o jogo
