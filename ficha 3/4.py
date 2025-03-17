def removeSpaces(texto):
    return texto.split()

texto = str(input("Indique um texto : "))
lista = removeSpaces(texto)
print(lista)
result = ""
for letra in lista:
    result = result + letra + " "
print(result)