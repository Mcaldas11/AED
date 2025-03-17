#Desenvolver um programa que leia um numero entre 1 e 99 e represente a sua linguagem binaria


n = int(input("Indique um numero inteiro positivo(1 a 99): "))

if 1 <= n <= 99:
    binario = bin(n)[2:]

print(f"Numero, {n}")
print(f"Resultado, {binario}")