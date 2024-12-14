import customtkinter

listaContinentes = ["Asia","America","Europa","Oceania","Africa"]

app = customtkinter.CTk()
app.title("Países do Mundo") #Nome da APP

appWidth= 600
appHeight = 300

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

labelPais = customtkinter.CTkLabel(app, text="País", fg_color="transparent", text_color="blue", font=("Helvetica",14))
labelPais.place(x=15,y=40)

labelContinente = customtkinter.CTkLabel(app, text="Continente", fg_color="transparent", text_color="blue", font=("Helvetica",14))
labelContinente.place(x=15,y=80)

labelHemisferio = customtkinter.CTkLabel(app, text="Hemisfério", fg_color="transparent", text_color="blue", font=("Helvetica",14))
labelHemisferio.place(x=15,y=120)

labelIdioma = customtkinter.CTkLabel(app, text="Idioma Oficial", fg_color="transparent", text_color="blue", font=("Helvetica",14))
labelIdioma.place(x=390,y=40)


# Inputs ---------------------------------------------------------

strPais = customtkinter.StringVar() #Criar variavel vazia
strPais.set("Portugal")             #Atribuir valor
entryPais = customtkinter.CTkEntry(app, placeholder_text="Indique um país", textvariable= strPais, width=150)
entryPais.place(x=100,y=40)

combContinente = customtkinter.CTkComboBox(app, values=listaContinentes, width=150, command="")
combContinente.place(x=100,y=80)
combContinente.set("Europa")

radioVariable = customtkinter.StringVar(value="Norte")

radioButton1 = customtkinter.CTkRadioButton(app, text="Norte", variable=radioVariable, value="Norte")
radioButton1.place(x=100,y=130)

radioButton1 = customtkinter.CTkRadioButton(app, text="Sul", variable=radioVariable, value="Sul")
radioButton1.place(x=100,y=160)

checkVar1 = customtkinter.StringVar(value="off")
checkVar2 = customtkinter.StringVar(value="on")
checkVar3 = customtkinter.StringVar(value="off")
checkVar4 = customtkinter.StringVar(value="off")

checkboxEN = customtkinter.CTkCheckBox(app, text="Inglês", variable=checkVar1, onvalue="on", offvalue="off")
checkboxPT = customtkinter.CTkCheckBox(app, text="Português", variable=checkVar2, onvalue="on", offvalue="off")
checkboxFR = customtkinter.CTkCheckBox(app, text="Francês", variable=checkVar3, onvalue="on", offvalue="off")
checkboxOT = customtkinter.CTkCheckBox(app, text="Outro", variable=checkVar4, onvalue="on", offvalue="off")

checkboxEN.place(x=350,y=70)
checkboxPT.place(x=450,y=70)
checkboxFR.place(x=350,y=100)
checkboxOT.place(x=450,y=100)

# Buttons ---------------------------------------------
btnGuardar = customtkinter.CTkButton(app, text="Guardar", command="",width=100, height=40, fg_color="gray")
btnGuardar.place(x=400,y=250)

btnLimpar = customtkinter.CTkButton(app, text="Limpar", command="",width=100, height=40, state="disabled", fg_color="gray")
btnLimpar.place(x=500,y=250)



app.mainloop()