import random
import time
import os

# Configurações do jogo
largura = 20
altura = 10
nave_pos = largura // 2
obstaculos = []
obstaculo_velocidade = 1

def desenhar():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(altura):
        linha = ''
        for x in range(largura):
            if (x, y) == (nave_pos, altura - 1):
                linha += 'A'  # Nave
            elif (x, y) in obstaculos:
                linha += 'X'  # Obstáculo
            else:
                linha += ' '
        print(linha)
    print("Use 'a' para mover para a esquerda, 'd' para mover para a direita.")

def atualizar_obstaculos():
    global obstaculos
    obstaculos = [(x, y + obstaculo_velocidade) for (x, y) in obstaculos if y + obstaculo_velocidade < altura]
    if random.random() < 0.3:  # 30% de chance de gerar um novo obstáculo
        obstaculos.append((random.randint(0, largura - 1), 0))

def checar_colisao():
    return (nave_pos, altura - 1) in obstaculos

def main():
    global nave_pos
    while True:
        desenhar()
        atualizar_obstaculos()

        if checar_colisao():
            print("Game Over!")
            break

        comando = input("Comando (a/d): ").strip().lower()
        if comando == 'a' and nave_pos > 0:
            nave_pos -= 1
        elif comando == 'd' and nave_pos < largura - 1:
            nave_pos += 1

        time.sleep(0.1)

if __name__ == "__main__":
    main()
