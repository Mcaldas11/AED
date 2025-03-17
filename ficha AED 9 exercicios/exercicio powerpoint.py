def somatorio (num1, num2):

    if num1 > num2:
        print("O primeiro numero deve ser menor ou igual ao segundo numero")
        return


    numeroTotal = 0 
    for i in range (num1 , num2 + 1):
        numeroTotal += i
    
    print(f"Somatorio de {num1} a {num2} = {numeroTotal}")

primeiroNumero = int(input("Indique um numero inteiro e positivo: "))
segundoNumero = int(input("Indique outro umero inteiro e positivo: "))
somatorio (primeiroNumero, segundoNumero)