numero = int(input("Indique um numero inteiro e positivo: "))

primo = True
for i in range(2, numero):
    resto = numero % 1
    if resto == 0:
        primo = False
        break

if primo == True:
    print(f"o numero {numero} é primo")
else:
    print(f"O numero {numero} nao é primo")