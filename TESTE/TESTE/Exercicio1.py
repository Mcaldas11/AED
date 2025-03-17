# IDENTIFICAÇÃO DO ESTUDANTE    
# Numero :40240221
# Ñome:Miguel Menicio Caldas

import random

def gerar_numero_aleatorio(min_valor, max_valor, num_gerados):
    #Gera um número aleatório entre min_valor e max_valor que ainda não foi gerado
    numeros_possiveis = [num for num in range(min_valor, max_valor + 1) if num not in num_gerados]
    if not numeros_possiveis:
        return None  
    return random.choice(numeros_possiveis)

def analisar_lista(numeros):
    #Analisa os numeros gerados e observa se sao divisiveis por 5 ou por 10
    return [num for num in numeros if num % 5 == 0 or num % 10 == 0]

def main():
    numeros_gerados = []  #Lista para guardar os numeros que foram gerados
    limite_minimo = 1  #Valor mínimo inicial
    limite_maximo = 100  #Valor máximo inicial

    while True:
        #Vai gerar um numero dentro dos limites minimos e máximos
        numero_gerado = gerar_numero_aleatorio(limite_minimo, limite_maximo, numeros_gerados)
        if numero_gerado is None:
            print("Não há mais números disponíveis para gerar!")
            break

        numeros_gerados.append(numero_gerado)
        print(f"Número gerado: {numero_gerado}")

        #Verifica se o número gerado aleatoriamente foi 100
        if numero_gerado == 100:
            print("O numero 100 foi gerado. O programa vai terminar")
            break

        #Pergunta se queremos gerar outro numero aleatorio
        resposta = input("Deseja gerar novo número (S/N)? ")
        while resposta not in ('S', 'N'):
            resposta = input("Insira 'S' para continuar a gerar ou 'N' para finalizar o programa: ")

        if resposta == 'N':
            break
        else:
            limite_minimo = numero_gerado + 1    #Continua a gerar numeros aleatorios entre o ultimo gerado ate 100

    #Mostra os resultados em ordem decrescente
    numeros_gerados.sort(reverse=True)  # Ordena a lista em ordem decrescente
    print("\nNúmeros gerados (ordem decrescente):", numeros_gerados)

    #Mostra os números divisíveis por 5 ou 10
    numeros_divisiveis = analisar_lista(numeros_gerados)
    print("Números divisíveis por 5 ou 10:", numeros_divisiveis)

if __name__ == "__main__":
    main()

