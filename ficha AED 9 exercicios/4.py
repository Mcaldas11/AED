#Criar um jogo para adivinhar um numero aleatorio


import random


while True:  # Loop para permitir jogar novamente
    num_secreto = random.randint(0, 50)
    tentativas = 0
    tentativas_maximas = 10

    print("\nBem-vindo ao jogo de adivinhação!")
    print("Você tem 10 tentativas para adivinhar o número entre 0 e 50.")

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

    jogar_novamente = input("Novo Jogo (S/N): ")
    if jogar_novamente.lower() != 's':
        print("Obrigado por jogar!!!")
        break