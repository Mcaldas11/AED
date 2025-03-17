def aboveAverage(listaNumeros):

    cont = 0
    media = sum(listaNumeros)/len(listaNumeros)
    for numero in listaNumeros:
        if numero > media:
            cont +=1
    return cont



listaNumeros = []

for i in range (10):
    numero = int(input("Indique o {:n}º numero: " .format(i+1)))
    listaNumeros.append(numero)


cont= aboveAverage(listaNumeros)
print("Exitem {:n} números acima da média".format(cont))