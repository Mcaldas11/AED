#Desenvolver um programa para observar se um numero é perfeito

num = int(input("Indique um numero inteiro e positivo: "))

soma_divisores = 0

for i in range (1, num):
    if num % i == 0:
        soma_divisores += i


if soma_divisores == num:
    print(f"{num} é um numero perfeito!!")
else:
    print(f"{num} nao e um numero perfeito!!")

