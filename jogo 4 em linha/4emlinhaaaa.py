import numpy as np

# Função para criar o tabuleiro
def criar_tabuleiro():
    return np.zeros((6, 7), dtype=int)

# Mostrar o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    print("\n")
    for linha in np.flip(tabuleiro, 0):
        print(" ".join([str(int(c)) if c != 0 else '.' for c in linha]))
    print("\n0 1 2 3 4 5 6\n")

# Verificar se a jogada é válida
def movimento_valido(tabuleiro, coluna):
    return tabuleiro[5][coluna] == 0

# Encontrar a próxima linha livre
def proxima_linha(tabuleiro, coluna):
    for linha in range(6):
        if tabuleiro[linha][coluna] == 0:
            return linha

# Colocar peça no tabuleiro
def colocar_peca(tabuleiro, linha, coluna, jogador):
    tabuleiro[linha][coluna] = jogador

# Verificar vitória
def verificar_vitoria(tabuleiro, peca):
    for i in range(42):  # Loop com uma variável para todo o tabuleiro (6x7=42)
        linha = i // 7
        coluna = i % 7
        if tabuleiro[linha][coluna] == peca:
            # Horizontal
            if coluna <= 3 and all(tabuleiro[linha][coluna + k] == peca for k in range(4)):
                return True
            # Vertical
            if linha <= 2 and all(tabuleiro[linha + k][coluna] == peca for k in range(4)):
                return True
            # Diagonal positiva
            if linha <= 2 and coluna <= 3 and all(tabuleiro[linha + k][coluna + k] == peca for k in range(4)):
                return True
            # Diagonal negativa
            if linha >= 3 and coluna <= 3 and all(tabuleiro[linha - k][coluna + k] == peca for k in range(4)):
                return True
    return False

# Função principal
def quatro_em_linha():
    print("Bem-vindo ao Jogo 4 em Linha!")
    
    # Solicitar nomes dos jogadores
    jogador1 = input("Nome do Jogador 1 (Peça 1): ")
    jogador2 = input("Nome do Jogador 2 (Peça 2): ")
    jogadores = {1: jogador1, 2: jogador2}
    
    tabuleiro = criar_tabuleiro()
    turno = 0
    
    mostrar_tabuleiro(tabuleiro)
    
    while True:
        jogador_atual = (turno % 2) + 1
        print(f"Turno de {jogadores[jogador_atual]}")
        
        try:
            coluna = int(input("Escolha uma coluna (0-6): "))
            if coluna < 0 or coluna > 6 or not movimento_valido(tabuleiro, coluna):
                print("Coluna inválida ou cheia! Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida! Digite um número entre 0 e 6.")
            continue
        
        # Jogada válida
        linha = proxima_linha(tabuleiro, coluna)
        colocar_peca(tabuleiro, linha, coluna, jogador_atual)
        mostrar_tabuleiro(tabuleiro)
        
        # Verificar vitória
        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f"Parabéns, {jogadores[jogador_atual]}! Você venceu!")
            break
        
        # Verificar empate
        if turno == 41:  # 42 jogadas máximas (6x7)
            print("O jogo terminou em empate!")
            break
        
        turno += 1

# Executar o jogo
if __name__ == "__main__":
    quatro_em_linha()
