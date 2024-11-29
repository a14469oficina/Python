x, y = random.randint(0, 3), random.randint(0, 3)  # Tabuleiro 4x4
            if tabuleiro[x][y] == " ":
                tabuleiro[x][y] = nave.letra
                break
