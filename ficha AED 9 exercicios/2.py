#Calcular a soma de todos os numeros pares entre o limite superior e o limite inferior

limiteInferior=int(input("Indique o limite inferior: "))
limiteSuperior=int(input("Indique o limite superior: "))

soma_pares = 0

for i in range(limiteInferior, limiteSuperior +1):
    if i % 2 == 0:
        soma_pares += i

print("A soma de todos os pares entre {:n} e {:n} é {:n}".format(limiteInferior, limiteSuperior, soma_pares))