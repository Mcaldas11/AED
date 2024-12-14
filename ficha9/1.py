import customtkinter

ficheiro = ".\\files\\texto.txt"

def guardarNota():
    fileNotas = open(ficheiro, "w", encoding="utf-8")
    linha = str(strTextbox.get("0.0", "end"))
    fileNotas.write(linha)
    fileNotas.close()

def limparNota():
    strTextbox.delete("0.0","end")

def lerNota():
    strTextbox.delete("0.0","end")
    linhasNota=[]
    fileNotas = open(ficheiro,"r",encoding="utf-8")
    for linha in fileNotas:
        linhasNota.append(linha)
    fileNotas.close()
    for linha in linhasNota:
        strTextbox.insert("end",linha)

fileNotas = open(ficheiro, "a", encoding="utf-8")
fileNotas.close()

app = customtkinter.CTk()
app.title("My Notepad") #Nome da APP

appWidth = 300
appHeight = 600

#Obter as dimensões do meu screen (em pixeis)
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

#App centrada no screen, em função das suas dimensões
x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

#app.configure(fg_color="")
app.resizable(False,False)

# Interface ------------------------------------------------------

# Labels ---------------------------------------------------------

labelTextbox = customtkinter.CTkLabel(app, text="Indique as suas notas", fg_color="transparent", text_color="blue", font=("Helvetica",14))
labelTextbox.place(x=75,y=40)

# Inputs ---------------------------------------------------------
#strTextbox = customtkinter.StringVar()
strTextbox = customtkinter.CTkTextbox(app, width=250, height=300, text_color="black",fg_color="white", border_color="gray")
strTextbox.place(x=25,y=80)


# Buttons ---------------------------------------------
btnGuardar = customtkinter.CTkButton(app, text="Guardar", command=guardarNota,width=250, height=50, fg_color="aqua",text_color="black")
btnGuardar.place(x=25,y=390)

btnLimpar = customtkinter.CTkButton(app, text="Limpar", command=limparNota,width=250, height=50, fg_color="aqua",text_color="black")
btnLimpar.place(x=25,y=450)

btnLer = customtkinter.CTkButton(app, text="Ler", command=lerNota,width=250, height=50, fg_color="aqua",text_color="black")
btnLer.place(x=25,y=510)

app.mainloop()
