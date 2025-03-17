#Criar um jogo para adivinhar um numero aleatorio


import random
num_secreto= random.randint(0,50)
tentativas = 0
tentativas_maximas = 10

for i in range(tentativas, tentativas_maximas):
    palpite = int(input("Indique o seu palpite: "))
    tentativas += 1



    if palpite < num_secreto :
        print("O número aleatório é maior")
    elif palpite > num_secreto :
        print("O número aleatório é menor")
    else :
        print("Acertou!!!")
        print(f"Parabens, acertou em {tentativas} tentativas")
        break

else :
    print(f"Voce esgotou as {tentativas_maximas} tentativas:( )")
    print(f"O numero secreto era {num_secreto}")