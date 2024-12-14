def inicializar_tabuleiro():
    """Inicializa o tabuleiro 7x6 vazio."""
    return [[' ' for _ in range(7)] for _ in range(6)]

def mostrar_tabuleiro(tabuleiro):
    """Exibe o tabuleiro no console."""
    print("\n  0   1   2   3   4   5   6")
    print("  -----------------------------")
    for linha in tabuleiro:
        print(" | ".join(linha) + " |")
        print("  -----------------------------")

def jogada_valida(tabuleiro, coluna):
    """Verifica se a jogada em uma coluna é válida (coluna não está cheia)."""
    return tabuleiro[0][coluna] == ' '

def realizar_jogada(tabuleiro, coluna, simbolo):
    """Realiza a jogada na coluna especificada pelo jogador."""
    for linha in reversed(tabuleiro):
        if linha[coluna] == ' ':
            linha[coluna] = simbolo
            return

def verificar_vitoria(tabuleiro, simbolo):
    """Verifica se há uma sequência de 4 em linha, coluna ou diagonal para o símbolo."""
    # Horizontal
    for linha in tabuleiro:
        for col in range(4):
            if all(linha[col + i] == simbolo for i in range(4)):
                return True
    # Vertical
    for col in range(7):
        for lin in range(3):
            if all(tabuleiro[lin + i][col] == simbolo for i in range(4)):
                return True
    # Diagonal (Cima-Esquerda para Baixo-Direita)
    for col in range(4):
        for lin in range(3):
            if all(tabuleiro[lin + i][col + i] == simbolo for i in range(4)):
                return True
    # Diagonal (Cima-Direita para Baixo-Esquerda)
    for col in range(3, 7):
        for lin in range(3):
            if all(tabuleiro[lin + i][col - i] == simbolo for i in range(4)):
                return True
    return False

def empate(tabuleiro):
    """Verifica se o tabuleiro está cheio e não há vencedores."""
    return all(tabuleiro[0][col] != ' ' for col in range(7))

def jogo_quatro_em_linha():
    """Funcao principal que executa o jogo Quatro em Linha (Versão 1: Dois jogadores)."""
    print("Bem-vindo ao Jogo Quatro em Linha!")

    # Inicialização de variáveis
    tabuleiro = inicializar_tabuleiro()
    jogador1 = input("Nome do Jogador 1: ")
    jogador2 = input("Nome do Jogador 2: ")
    simbolo1 = 'X'
    simbolo2 = 'O'

    mostrar_tabuleiro(tabuleiro)
    jogador_atual = jogador1
    simbolo_atual = simbolo1

    # Loop principal do jogo
    while True:
        print(f"\n{jogador_atual} ({simbolo_atual}), é sua vez.")
        while True:
            try:
                coluna = int(input("Escolha uma coluna (0-6): "))
                if 0 <= coluna <= 6 and jogada_valida(tabuleiro, coluna):
                    break
                else:
                    print("Coluna inválida ou cheia. Tente novamente.")
            except ValueError:
                print("Entrada inválida! Digite um número entre 0 e 6.")

        realizar_jogada(tabuleiro, coluna, simbolo_atual)
        mostrar_tabuleiro(tabuleiro)

        # Verifica vitória
        if verificar_vitoria(tabuleiro, simbolo_atual):
            print(f"\nParabéns! {jogador_atual} venceu!")
            break

        # Verifica empate
        if empate(tabuleiro):
            print("\nO jogo terminou em empate!")
            break

        # Alterna o jogador
        if jogador_atual == jogador1:
            jogador_atual = jogador2
            simbolo_atual = simbolo2
        else:
            jogador_atual = jogador1
            simbolo_atual = simbolo1

if __name__ == "__main__":
    jogo_quatro_em_linha()
