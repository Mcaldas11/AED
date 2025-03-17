#Calcular o fatorial de um numero  sem a função


numero = int(input("Indique um numero: "))

if numero<0:
    print("Indique um numero maior que 0")
else:
    fatorial=1
    for i in range(numero, 1, -1):
        fatorial*=i
    
print("Fatorial de {0} é {1}".format(numero, fatorial))
