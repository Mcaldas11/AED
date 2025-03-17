def shortName(nome):
    nomes= nome.split()
    primeiroNome = nomes[0]
    ultimoNome = nomes[-1]

    return f"{primeiroNome} {ultimoNome}"

nome = input("Indique o seu nome completo: ")
print (shortName(nome))