def standardName(nome):
    nomes= nome.split()
    
    primeiroNome = nomes[0]
    nomeIntercalados = [parte[0] + '.' for parte in nomes[1:-1]] #Ciclo para comecar apos o primeiro nome a terminar quando o ultimo nome é detectado
    ultimoNome = nomes[-1]


    nomeNormalizado = primeiroNome + ' ' # Espaço entre os nomes 

    for abreviatura in nomeIntercalados:
        nomeNormalizado += abreviatura + ' ' #Adicionar as abreviaturas apos um espaço entre os nomes

    
    nomeNormalizado += ultimoNome #Finalizar o nome com o primeiro as abreviaturas e o ultimo

    return nomeNormalizado.strip()

nome_usuario = input("Digite um nome completo: ")
nome_normalizado = standardName(nome_usuario)
print(nome_normalizado)
