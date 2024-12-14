import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Função para calcular o IMC
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Converter altura para metros
        bmi = round(weight / (height ** 2), 2)
        bmi_label.config(text=f"Seu IMC: {bmi}")

        # Categorias de IMC
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 25:
            category = "Peso normal"
        elif 25 <= bmi < 30:
            category = "Sobrepeso"
        elif 30 <= bmi < 35:
            category = "Obesidade Grau I"
        elif 35 <= bmi < 40:
            category = "Obesidade Grau II"
        else:
            category = "Obesidade Grau III"

        category_label.config(text=f"Categoria: {category}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Configuração da aplicação
app = ctk.CTk()
app.title("Simulador de IMC")
app.geometry("325x670")

# Frame superior
frame_top = ctk.CTkFrame(app, width=300, height=150)
frame_top.pack(pady=10)

# Frame inferior
frame_bottom = ctk.CTkFrame(app, width=300, height=100)
frame_bottom.pack(pady=10)

# Título do Frame superior
frame_title = ctk.CTkLabel(frame_top, text="Calculadora de IMC", font=("Arial", 18, "bold"))
frame_title.pack(pady=5)

# Entradas de peso e altura
weight_label = ctk.CTkLabel(frame_top, text="Peso (kg):", font=("Arial", 12))
weight_label.pack(anchor="w", padx=10)

weight_entry = ctk.CTkEntry(frame_top, width=150)
weight_entry.pack(pady=5)

height_label = ctk.CTkLabel(frame_top, text="Altura (cm):", font=("Arial", 12))
height_label.pack(anchor="w", padx=10)

height_entry = ctk.CTkEntry(frame_top, width=150)
height_entry.pack(pady=5)

# Botão com imagem
try:
    img = Image.open(".\\images\\imc.gif")
    img = img.resize((280, 160), Image.ANTIALIAS)  # Redimensiona a imagem
    imc_image = ImageTk.PhotoImage(img)

    image_button = ctk.CTkButton(app, image=imc_image, text="", width=280, height=160, command=calculate_bmi)
    image_button.pack(pady=10)
except FileNotFoundError:
    messagebox.showerror("Erro", "Imagem não encontrada. Certifique-se de que o caminho está correto.")

# Resultados no Frame inferior
bmi_label = ctk.CTkLabel(frame_bottom, text="Seu IMC: --", font=("Arial", 14))
bmi_label.pack(pady=5)

category_label = ctk.CTkLabel(frame_bottom, text="Categoria: --", font=("Arial", 14))
category_label.pack(pady=5)

# Inicia o loop principal da aplicação
app.mainloop()
