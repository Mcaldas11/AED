def maior (*numeros : int):


    maximo = numeros [0]
    for i in range(len(numeros)):
        if numeros [i] > maximo:
             maximo = numeros [i]
    return maximo


print(maior(10, 20 , 12))
print(maior(0, 20 , 13 , 15))
    