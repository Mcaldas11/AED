# Biblioteca Tkinter: UI
import customtkinter 
from PIL import Image, ImageTk
from tkinter import filedialog   # filedialog boxes
from tkinter import ttk

global listaImagens
listaImagens= []
indiceAtual = 0

#----------------------------------------------------
# GUI -----------------------------------------------
#----------------------------------------------------
def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    # App centrada no screen, em função das suas dimensões# encontrar o 
    x = (screenWidth/2) - (appWidth/2)
    y= (screenHeight/2) - (appHeight/2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False) 

def selecionar_imagens():
    """
    Abre uma caixa  de dialogo para selecionar a imagem  e adiciona os caminhos á lista
    """
    global listaImagens
    arquivos =filedialog.askopenfilenames(
        title="Selecionar imagens",
        filetypes=[("Imagens","*.png;*.jpg;*.jpeg")]
    )
    if arquivos:
        listaImagens.extend(arquivos)
        atualizar_treeview()

def atualizar_treeview():
    """
    Atualiza o Treeview para exibir a lista de imagens.
    """
    treeview.delete(*treeview.get_children())
    for i , caminho in enumerate(listaImagens):
        treeview.insert("","end",iid=i, text= caminho.split("/")[-1])

def exibir_imagem(indice):
    """
    Exibe a imagem no frame, com base no índice fornecido.
    """
    global indiceAtual
    if listaImagens:
        try:
            caminho = listaImagens[indice]
            imagem = Image.open(caminho)
            imagem = imagem.resize((250, 250))  # Redimensiona a imagem
            imagem_tk = ImageTk.PhotoImage(imagem)
            label_imagem.configure(image=imagem_tk)
            label_imagem.image = imagem_tk  # Referência para evitar garbage collection
            indiceAtual = indice
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

def proxima_imagem():
    """
    Mostra a proxima imagem 
    """
    global indiceAtual
    if listaImagens and indiceAtual < len(listaImagens) - 1:
        exibir_imagem(indiceAtual + 1)

def imagem_anterior():
    global indiceAtual
    if listaImagens and indiceAtual > 0:
        exibir_imagem(indiceAtual - 1)


def remover_imagem():
    """
    Remove a imagem da treeview e da lista
    """
    global listaImagens, indiceAtual
    selecionado = treeview.selection()
    if selecionado:
        indice = int(selecionado[0])
        listaImagens.pop(indice)
        atualizar_treeview()
        if listaImagens:
            novo_indice = min(indiceAtual, len(listaImagens) - 1)
            exibir_imagem(novo_indice)
        else:
            label_imagem.configure(image="")


#-----Arranque da aplicação --------------------------------
# INTERFACE GRAFICA DA APLICAÇÃO 
app=customtkinter.CTk()   # invoca classe Ctk , cria a "main window"
renderWindow(700, 450, "my Album!")

#Frame para exibir a imagem

frame_imagem = customtkinter.CTkFrame(app, width=260, height=260)
frame_imagem.place(x=20, y = 20)
label_imagem = customtkinter.CTkLabel(frame_imagem, text="")
label_imagem.pack(expand=True)


#Treeview para imagens

treeview = ttk.Treeview(app)
treeview.heading("#0", text="Imagens Selecionadas")
treeview.place(x=300,y = 20 , width=380, height=300)
#Botões

botao_selecionar = customtkinter.CTkButton(app, text="Selecionar Imagens", command=selecionar_imagens)
botao_selecionar.place(x=20, y=300)

botao_remover = customtkinter.CTkButton(app, text="Remover Imagem", command=remover_imagem)
botao_remover.place(x=160, y=300)

botao_anterior = customtkinter.CTkButton(app, text="Anterior", command=imagem_anterior)
botao_anterior.place(x=20, y=350)

botao_proximo = customtkinter.CTkButton(app, text="Próxima", command=proxima_imagem)
botao_proximo.place(x=160, y=350)



app.mainloop()   # event listening loop by calling the mainloop()