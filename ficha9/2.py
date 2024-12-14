import customtkinter as ctk

# Função para calcular o peso ideal
def calcular_peso_ideal():
    try:
        altura = float(entry_altura.get())  # Obter altura inserida
        if genero_var.get() == "Masculino":
            k = 4
        elif genero_var.get() == "Feminino":
            k = 2
        else:
            label_resultado.configure(text="Selecione um gênero!", text_color="red")
            return

        # Fórmula: (altura - 100) - (altura - 150) / k
        peso_ideal = (altura - 100) - ((altura - 150) / k)
        label_resultado.configure(
            text=f"Peso Ideal em Kg: {peso_ideal:.1f}", text_color="green"
        )
    except ValueError:
        label_resultado.configure(text="Insira uma altura válida!", text_color="red")

# Configuração da janela principal
app = ctk.CTk()
app.title("Simulador de Peso Ideal")
app.geometry("370x430")

# Label de título
label_titulo = ctk.CTkLabel(app, text="Simulador de Peso Ideal", font=("Arial", 18))
label_titulo.pack(pady=10)

# Entrada para altura
label_altura = ctk.CTkLabel(app, text="Altura em cm:", font=("Arial", 14))
label_altura.pack(pady=5)

entry_altura = ctk.CTkEntry(app, width=200, placeholder_text="Ex: 180")
entry_altura.pack(pady=5)

# Opções de gênero
label_genero = ctk.CTkLabel(app, text="Gênero:", font=("Arial", 14))
label_genero.pack(pady=5)

genero_var = ctk.StringVar(value="")  # Variável para armazenar a seleção do gênero
radio_masculino = ctk.CTkRadioButton(app, text="Masculino", variable=genero_var, value="Masculino")
radio_masculino.pack()

radio_feminino = ctk.CTkRadioButton(app, text="Feminino", variable=genero_var, value="Feminino")
radio_feminino.pack()

# Botão para calcular peso ideal
btn_calcular = ctk.CTkButton(
    app, text="Calcular Peso Ideal", width=260, height=80, fg_color="blue", command=calcular_peso_ideal
)
btn_calcular.pack(pady=15)

# Resultado
label_resultado = ctk.CTkLabel(app, text="", font=("Arial", 16))
label_resultado.pack(pady=10)

# Iniciar a aplicação
app.mainloop()
