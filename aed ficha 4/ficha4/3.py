def positiveList(listPontuacao):
    novaList = []
    for i in range(0, len(listPontuacao)):
        if listPontuacao[i] >= 10:
            novaList.append(listPontuacao[i])
    return novaList          #devolve nova lista com pontuacoes positivas


listPontuacao = []
#ler a pontuaçao de 10 participantes de 0 a 20

i=0
while i <10:
    try:
        pontuacao = int(input("Pontuacao do {:n}º participante:".format(i+1)))
        if pontuacao <0 or pontuacao > 20:
            raise ValueError()
    except ValueError:
        print("O valor nao esta dentro dos limites tente novamente!")
    except:
        print("O valor inserido não é valido")
    else:
        listPontuacao.append(pontuacao)
        i += 1
    
print("Pontuacoes positivas: ", positiveList(listPontuacao))
