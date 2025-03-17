#Desenvolver um programa que le n Numeros e diante esses numeros identifica o segundo maior

import random

numero_inserido = int(input("Quantos números deseja ler?: "))

maior = 0
segundo_maior = 0

contador = numero_inserido

while contador > 0:
    numero_atual = random.randint(1, 99)
    print(f"Número: {numero_atual}")

    if numero_atual > maior :
        segundo_maior = maior
        maior = numero_atual
    elif numero_atual > segundo_maior and numero_atual != maior:
        segundo_maior = numero_atual
    
    contador -= 1

print(f"O segundo maior numero na lista lida é: {segundo_maior}")

