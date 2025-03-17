def searchNumber(lista, pesquisa):
    posicoes = []

    for i in range(len(lista)):
        if lista[i] == pesquisa:
            posicoes.append(i)
    
    if posicoes:
        return posicoes
    else:
        return "O valor de pesquisa não foi encontrado na lista."

lista = []
i = 0

while i < 10:
    try:
        numero = int(input("Indique o {:n}º número: ".format(i + 1)))
        lista.append(numero)
        i += 1 
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

try:
    pesquisa = int(input("Digite o valor que deseja pesquisar na lista: "))

    resultado = searchNumber(lista, pesquisa)

    if isinstance(resultado, list):
        print(f"O valor {pesquisa} foi encontrado nas posições: {resultado}")
    else:
        print(resultado)

except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro para a pesquisa.")
