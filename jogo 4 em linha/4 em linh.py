import customtkinter as ctk
import numpy as np
import random

# Configurações principais
ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER1 = 1
PLAYER2 = 2

class QuatroEmLinha(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("4 em Linha")
        self.geometry("800x800")
        self.tabuleiro = None
        self.turno = None
        self.modo = None
        self.dificuldade = None
        self.botoes = None
        self.jogador1_nome = "Jogador 1"
        self.jogador2_nome = "Jogador 2"

        self.frames = {}
        self.criar_menu_inicial()

    def criar_menu_inicial(self):
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True)

        ctk.CTkLabel(frame, text="4 em Linha", font=("Arial", 40)).pack(pady=20)

        ctk.CTkButton(frame, text="Multijogador", command=self.menu_nomes).pack(pady=10)
        ctk.CTkButton(frame, text="Contra CPU", command=self.menu_dificuldade).pack(pady=10)

        self.frames["menu_inicial"] = frame

    def menu_nomes(self):
        self.frames["menu_inicial"].pack_forget()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True)

        ctk.CTkLabel(frame, text="Digite os Nomes dos Jogadores", font=("Arial", 30)).pack(pady=20)

        self.entry_jogador1 = ctk.CTkEntry(frame, placeholder_text="Nome do Jogador 1")
        self.entry_jogador1.pack(pady=10)
        self.entry_jogador2 = ctk.CTkEntry(frame, placeholder_text="Nome do Jogador 2")
        self.entry_jogador2.pack(pady=10)

        ctk.CTkButton(frame, text="Iniciar Jogo", command=self.confirmar_nomes).pack(pady=10)

        self.frames["menu_nomes"] = frame

    def confirmar_nomes(self):
        nome1 = self.entry_jogador1.get().strip()
        nome2 = self.entry_jogador2.get().strip()

        if nome1:
            self.jogador1_nome = nome1
        if nome2:
            self.jogador2_nome = nome2

        self.iniciar_jogo("multijogador")

    def menu_dificuldade(self):
        self.frames["menu_inicial"].pack_forget()
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True)

        ctk.CTkLabel(frame, text="Escolha a Dificuldade", font=("Arial", 30)).pack(pady=20)
        ctk.CTkButton(frame, text="Fácil", command=lambda: self.iniciar_jogo("cpu", "facil")).pack(pady=10)
        ctk.CTkButton(frame, text="Normal", command=lambda: self.iniciar_jogo("cpu", "normal")).pack(pady=10)
        ctk.CTkButton(frame, text="Difícil", command=lambda: self.iniciar_jogo("cpu", "dificil")).pack(pady=10)

        self.frames["menu_dificuldade"] = frame

    def iniciar_jogo(self, modo, dificuldade=None):
        self.modo = modo
        self.dificuldade = dificuldade
        self.turno = PLAYER1
        self.tabuleiro = self.criar_tabuleiro()

        for frame in self.frames.values():
            frame.pack_forget()

        self.jogo_frame = ctk.CTkFrame(self)
        self.jogo_frame.pack(expand=True)
        self.botoes = [[None for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT):
                btn = ctk.CTkButton(self.jogo_frame, text="", width=70, height=70, font=("Arial", 20),
                                    command=lambda col=c: self.realizar_jogada_interface(col))
                btn.grid(row=r, column=c, padx=5, pady=5)
                self.botoes[r][c] = btn

        self.status_label = ctk.CTkLabel(
            self, text=f"{self.jogador1_nome} (Vermelho) é o próximo!", font=("Arial", 20)
        )
        self.status_label.pack(pady=20)

    def criar_tabuleiro(self):
        return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

    def realizar_jogada_interface(self, col):
        if not self.validar_jogada(col):
            return

        row = self.encontrar_linha_vazia(col)
        self.realizar_jogada(row, col, self.turno)
        self.atualizar_tabuleiro()

        if self.verificar_vitoria(self.turno):
            vencedor = self.jogador1_nome if self.turno == PLAYER1 else self.jogador2_nome
            if self.modo == "cpu" and self.turno == PLAYER2:
                vencedor = "CPU"
            self.fim_de_jogo(f"{vencedor} venceu!")
            return

        if not np.any(self.tabuleiro == 0):  # Verificar empate
            self.fim_de_jogo("Empate!")
            return

        self.turno = PLAYER2 if self.turno == PLAYER1 else PLAYER1
        proximo_jogador = self.jogador1_nome if self.turno == PLAYER1 else self.jogador2_nome
        cor = "Vermelho" if self.turno == PLAYER1 else "Amarelo"

        self.status_label.configure(text=f"{proximo_jogador} ({cor}) é o próximo!")

        if self.modo == "cpu" and self.turno == PLAYER2:
            col_cpu = self.cpu_movimento()
            self.realizar_jogada_interface(col_cpu)

    def atualizar_tabuleiro(self):
        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT):
                if self.tabuleiro[r][c] == PLAYER1:
                    self.botoes[r][c].configure(fg_color="red", text="O")
                elif self.tabuleiro[r][c] == PLAYER2:
                    self.botoes[r][c].configure(fg_color="yellow", text="X")

    def fim_de_jogo(self, mensagem):
        self.status_label.configure(text=mensagem)
        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT):
                self.botoes[r][c].configure(state="disabled")
        ctk.CTkButton(self, text="Reiniciar", command=self.reiniciar, font=("Arial", 20)).pack(pady=20)

    def reiniciar(self):
        self.destroy()
        QuatroEmLinha().mainloop()

    # Lógica do jogo
    def validar_jogada(self, col):
        return self.tabuleiro[0][col] == 0

    def encontrar_linha_vazia(self, col):
        for r in range(ROW_COUNT - 1, -1, -1):
            if self.tabuleiro[r][col] == 0:
                return r
        return None

    def realizar_jogada(self, row, col, jogador):
        self.tabuleiro[row][col] = jogador

    def verificar_vitoria(self, jogador):
        # Verificação horizontal, vertical e diagonal
        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT - 3):
                if all(self.tabuleiro[r, c:c + 4] == jogador):
                    return True
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT):
                if all(self.tabuleiro[r:r + 4, c] == jogador):
                    return True
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                if all([self.tabuleiro[r + i][c + i] == jogador for i in range(4)]):
                    return True
        for r in range(3, ROW_COUNT):
            for c in range(COLUMN_COUNT - 3):
                if all([self.tabuleiro[r - i][c + i] == jogador for i in range(4)]):
                    return True
        return False

    def cpu_movimento(self):
        if self.dificuldade == "facil":
            # CPU aleatória
            return random.choice([c for c in range(COLUMN_COUNT) if self.validar_jogada(c)])
        
        elif self.dificuldade == "normal":
            # Verifica se CPU pode ganhar em uma jogada
            for col in range(COLUMN_COUNT):
                if self.validar_jogada(col):
                    row = self.encontrar_linha_vazia(col)
                    self.tabuleiro[row][col] = PLAYER2
                    if self.verificar_vitoria(PLAYER2):
                        self.tabuleiro[row][col] = 0
                        return col
                    self.tabuleiro[row][col] = 0
            
            # Caso contrário, escolha aleatória
            return random.choice([c for c in range(COLUMN_COUNT) if self.validar_jogada(c)])
        
        elif self.dificuldade == "dificil":
            # 1. Verifica se CPU pode ganhar em uma jogada
            for col in range(COLUMN_COUNT):
                if self.validar_jogada(col):
                    row = self.encontrar_linha_vazia(col)
                    self.tabuleiro[row][col] = PLAYER2
                    if self.verificar_vitoria(PLAYER2):
                        self.tabuleiro[row][col] = 0
                        return col
                    self.tabuleiro[row][col] = 0
            
            # 2. Verifica se o jogador pode ganhar e bloqueia
            for col in range(COLUMN_COUNT):
                if self.validar_jogada(col):
                    row = self.encontrar_linha_vazia(col)
                    self.tabuleiro[row][col] = PLAYER1
                    if self.verificar_vitoria(PLAYER1):
                        self.tabuleiro[row][col] = 0
                        return col
                    self.tabuleiro[row][col] = 0
            
            # 3. Escolhe a melhor coluna (ex: meio é prioritário)
            colunas_prioritarias = [3, 2, 4, 1, 5, 0, 6]
            for col in colunas_prioritarias:
                if self.validar_jogada(col):
                    return col
            
            # 4. Caso tudo falhe, escolha aleatória
            return random.choice([c for c in range(COLUMN_COUNT) if self.validar_jogada(c)])

if __name__ == "__main__":
    app = QuatroEmLinha()
    app.mainloop()
