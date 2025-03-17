def positiveList(listPontuacao, listNome):
    novaListPont = []
    novaListNome = []
    for i in range(0, len(listPontuacao)):
        if listPontuacao[i] >= 10:
            novaListPont.append(listPontuacao[i])
            novaListNome.append(listNome[i])
    return novaListPont,  novaListNome          #devolve nova lista com pontuacoes positivas


listPontuacao = []
listNome = []
#ler a pontuaçao de 10 participantes de 0 a 20

i=0
while i <10:
    try:
        pontuacao = int(input("Pontuacao do {:n}º participante:".format(i+1)))
        nome = input("Insira o nome do {:n} participante: ".format(i+1))
        if pontuacao <0 or pontuacao > 20:
            raise ValueError()
    except ValueError:
        print("O valor nao esta dentro dos limites tente novamente!")
    except:
        print("O valor inserido não é valido")
    else:
        listPontuacao.append(pontuacao)
        listNome.append(nome)
        i += 1
    
novaListPont, novaListNome = positiveList(listPontuacao, listNome)
print("Pontuações positivas: ", novaListPont)
print("Nomes dos participantes com pontuações positivas: ", novaListNome)
