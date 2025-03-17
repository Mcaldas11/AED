# Biblioteca Tkinter: UI
import os
import customtkinter
import CTkMessagebox             # MessageBox
from tkinter import ttk          # Treeview
from tkinter import filedialog   # filedialog boxes
from PIL import ImageTk, Image    # Imagens .jpg ou .png
import datetime

# IDENTIFICAÇÃO DO ESTUDANTE    
# Numero :40240221
# Nome:Miguel Menicio Caldas

# Funções solicitadas

# 2.2 Função para exibir as provas nos arquivos
def viewTrails():
    tree.delete(*tree.get_children())  # Limpar os dados existentes na Treeview
    num_provas = 0

    if ck1.get():  # Se "Trail Curto" estiver ativado
        try:
            file = open("./ficheiros/trails.txt", "r", encoding="utf-8")
            for line in file:
                tree.insert("", "end", values=line.strip().split(";"))
                num_provas += 1
            file.close()
        except Exception as e:
            CTkMessagebox.show_error("Erro", f"Erro ao abrir 'trails.txt': {e}")

    if ck2.get():  # Se "Ultra Trail" estiver ativado
        try:
            file = open("./ficheiros/ultratrails.txt", "r", encoding="utf-8")
            for line in file:
                tree.insert("", "end", values=line.strip().split(";"))
                num_provas += 1
            file.close()
        except Exception as e:
            CTkMessagebox.show_error("Erro", f"Erro ao abrir 'ultratrails.txt': {e}")

    txtNumProvas.configure(state="normal")
    txtNumProvas.delete(0, "end")
    txtNumProvas.insert(0, str(num_provas))
    txtNumProvas.configure(state="readonly")


# 2.3 Função para ordenar em ordem ascendente
def ordAsc():
    data = sorted(tree.get_children(), key=lambda x: tree.item(x)["values"][0].lower())
    reorganize_tree(data)

def ordDesc():
    data = sorted(tree.get_children(), key=lambda x: tree.item(x)["values"][0].lower(), reverse=True)
    reorganize_tree(data)

def reorganize_tree(data):
    items = [tree.item(i)["values"] for i in data]
    tree.delete(*tree.get_children())
    for item in items:
        tree.insert("", "end", values=item)


# 2.5 Função para notificar a prova mais próxima
def notificacoes():
    provas = [
        (item["values"][1], item["values"][0])
        for item in (tree.item(i) for i in tree.get_children())
    ]
    provas.sort(key=lambda x: datetime.datetime.strptime(x[0], "%d-%m-%Y"))
    prova_proxima = provas[0] if provas else None

    if prova_proxima:
        CTkMessagebox.CTkMessagebox(title="Notificação", message= f"Prova mais próxima: {prova_proxima[1]} em {prova_proxima[0]}", icon="info", option_1="Ok")
    else:
        CTkMessagebox.CTkMessagebox(title="Notificação", message="Nenhuma prova disponível.", icon="info", option_1="Ok")


# 2.7 Função para selecionar imagem
def selecionarImagem():
    file_path = filedialog.askopenfilename(initialdir="./imagens", title="Selecionar Imagem",
                                           filetypes=(("Arquivos de imagem", "*.png;*.jpg"), ("Todos os arquivos", "*.*")))
    if file_path:
        img = customtkinter.CTkImage(Image.open(file_path), size=(180, 180))
        btnImagem.configure(image=img)


# 2.8 Função para adicionar aos favoritos
def addFavoritos():
    selected = tree.selection()
    if selected:
        prova = tree.item(selected[0])["values"]
        lboxFav.insert("end", "; ".join(prova))
    else:
        CTkMessagebox.CTkMessagebox(title="Atenção", message="Selecione uma prova antes de adicionar aos favoritos.", icon="warning", option_1="Ok")

def fileFavoritos():
    favoritos = lboxFav.get("1.0", "end").strip()
    if favoritos:
        os.makedirs("ficheiros", exist_ok=True)
        f = open("ficheiros/favoritos.txt", "w")
        f.write(favoritos)
        f.close()
        CTkMessagebox.CTkMessagebox(title="Sucesso", message="Favoritos guardados em ficheiros/favoritos.txt")
    else:
        CTkMessagebox.CTkMessagebox(title="Atenção", message="Nenhum favorito para guardar.")


# GUI: Interface Gráfica
def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    x = (screenWidth / 2) - (appWidth / 2)
    y = (screenHeight / 2) - (appHeight / 2)
    app.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")
    app.resizable(False, False)


# Inicialização
app = customtkinter.CTk()
renderWindow(1000, 500, "Trails App")

# 2.1 CheckBox
ck1_var = customtkinter.BooleanVar()
ck2_var = customtkinter.BooleanVar(value=True)

ck1 = customtkinter.CTkCheckBox(app, text="Trail Curto", variable=ck1_var)
ck2 = customtkinter.CTkCheckBox(app, text="Ultra Trail", variable=ck2_var)
ck1.place(x=50, y=20)
ck2.place(x=150, y=20)

# Botões e TreeView
btnImage1 = customtkinter.CTkImage(Image.open(".\\imagens\\pesquisar.png"), size=(35, 35))
btnSearch = customtkinter.CTkButton(app, width=35, height=35, image=btnImage1, text="", fg_color="transparent", command=viewTrails)
btnSearch.place(x=300, y=12)

btnImage2 = customtkinter.CTkImage(Image.open(".\\imagens\\asc.png"), size=(35, 35))
btnAsc = customtkinter.CTkButton(app, width=35, height=35, image=btnImage2, text="", fg_color="transparent", command=ordAsc)
btnAsc.place(x=400, y=12)

btnImage3 = customtkinter.CTkImage(Image.open(".\\imagens\\desc.png"), size=(35, 35))
btnDesc = customtkinter.CTkButton(app, width=35, height=35, image=btnImage3, text="", fg_color="transparent", command=ordDesc)
btnDesc.place(x=500, y=12)

btnImage4 = customtkinter.CTkImage(Image.open(".\\imagens\\notificacao.png"), size=(40, 40))
btnNotificacoes = customtkinter.CTkButton(app, width=48, height=48, image=btnImage4, text="", fg_color="transparent", command=notificacoes)
btnNotificacoes.place(x=600, y=12)

lblCircuitos = customtkinter.CTkLabel(app, text="Os meus circuitos", font=("Helvetica", 14), text_color="red")
lblCircuitos.place(x=200, y=50)

# TreeView
columns = ("Prova", "Data", "Local", "Km")
tree = ttk.Treeview(app, columns=columns, show="headings", height=12, selectmode="browse")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")
tree.place(x=20, y=100)

lblNumProvas = customtkinter.CTkLabel(app, text="Nº de provas", font=("Helvetica", 13))
lblNumProvas.place(x=50, y=320)

txtNumProvas = customtkinter.CTkEntry(app, width=50)
txtNumProvas.place(x=150, y=320)
txtNumProvas.configure(state="readonly")

btnSelecionarImg = customtkinter.CTkButton(app, width=45, height=45, text="Selecionar Imagem", fg_color="black", text_color="cyan", command=selecionarImagem)
btnSelecionarImg.place(x=180, y=430)

img = customtkinter.CTkImage(Image.open(".\\imagens\\img1.png"), size=(180, 180))
btnImagem = customtkinter.CTkButton(app, width=180, height=180, image=img, text="", fg_color="transparent")
btnImagem.place(x=330, y=300)

btnAddFav = customtkinter.CTkButton(app, text="Adicionar >>\n Favoritos", height=45, fg_color="black", text_color="cyan", command=addFavoritos)
btnAddFav.place(x=550, y=150)

frame1 = customtkinter.CTkFrame(app, width=300, height=500)
frame1.place(x=700, y=1)

lblFav = customtkinter.CTkLabel(frame1, text="Favoritos", font=("Helvetica", 14))
lblFav.place(x=100, y=30)

lboxFav = customtkinter.CTkTextbox(frame1, width=250, height=250, fg_color="gray", text_color="white")
lboxFav.place(x=20, y=60)

btnGuardarFav = customtkinter.CTkButton(frame1, text="Guardar Favoritos", height=90, width=250, fg_color="black", text_color="cyan", command=fileFavoritos)
btnGuardarFav.place(x=20, y=320)

app.mainloop()
