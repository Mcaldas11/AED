import random

def generateNumbers(limInf, limSup, qt):
    cont = 0
    listaNumero = []
    while cont < qt:
            numero= random.randint(limInf, limSup)
            if numero not in listaNumero:
                    listaNumero.append(numero)
                    cont+=1
    return listaNumero
resposta = "S"
while resposta.upper() == "S":
    print("\nNumeros: " ,generateNumbers (1, 50, 5))
    print("\nEstrelas: " ,generateNumbers (1, 12, 2))
    resposta = input("Gerar nova chave(S/N)?:")


