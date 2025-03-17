

def maiorFaturacao(faturacao, meses):
    maior = max(faturacao)
    pos = faturacao.index(maior)

    return f"o mes de maior faturacao foi: {meses[pos]}"

def menorFaturacao(faturacao, meses):
    menor = min(faturacao)
    pos = faturacao.index(menor)

    return f"o mes de menor faturacao foi: {meses[pos]}"

def mediaFaturacao(faturacao):
    return sum (faturacao)/len(faturacao)

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto' , 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

faturacao = []
for i in range (12):
    faturacao.append(int(input("Indique a faturacao do mes de {:s}: ".format(meses[i]))))

print(maiorFaturacao(faturacao, meses))
print(menorFaturacao(faturacao, meses))
print(mediaFaturacao(faturacao ))
    

