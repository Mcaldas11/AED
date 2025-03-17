import os

# Função para ler os dados do ficheiro
def ler_ficheiro():
    ficheiro_path = '.\\temperatura.txt'
    if not os.path.exists(ficheiro_path):
        print("O ficheiro temperatura.txt não foi encontrado!")
        return []
    
    with open(ficheiro_path, 'r') as f:
        dados = f.readlines()
    
    # Limpa os dados e separa os campos (data, hora, temperatura)
    return [linha.strip().split(';') for linha in dados]

# Função para consultar dados por data
def consultar_por_data():
    dados = ler_ficheiro()
    if not dados:
        return
    
    data_procurada = input("Introduza a data (AAAA-MM-DD): ").strip()
    
    # Filtra os dados com base na data (primeira parte do campo)
    encontrados = [linha for linha in dados if linha[0] == data_procurada]
    
    if encontrados:
        print(f"\n\tDados para a data {data_procurada}:")
        print("\n\tHora\t\tTemperatura (°C)")
        print("--------------------------------------------")
        for registo in encontrados:
            print(f"\t{registo[1]}\t\t{registo[2]}°C")
    else:
        print(f"Não foram encontrados dados para a data {data_procurada}.")

# Função para calcular a temperatura mínima, máxima e média
def consultar_estatisticas():
    dados = ler_ficheiro()
    if not dados:
        return
    
    temperaturas = []
    
    # Tenta converter a temperatura para float e adiciona à lista, caso contrário ignora
    for registo in dados:
        try:
            temperaturas.append(float(registo[2]))  # Converte a temperatura para float
        except ValueError:
            print(f"Aviso: Temperatura inválida na linha: {registo}. Ignorando esta linha.")
    
    if temperaturas:
        temperatura_min = min(temperaturas)
        temperatura_max = max(temperaturas)
        temperatura_media = sum(temperaturas) / len(temperaturas)
        
        # Apresentação das estatísticas com design similar ao exemplo fornecido
        print("\n\t\tEstatísticas de Temperatura")
        print("---------------------------------------------------")
        print(f"\tTemperatura Mínima\t: {temperatura_min}°C")
        print(f"\tTemperatura Máxima\t: {temperatura_max}°C")
        print(f"\tTemperatura Média\t: {temperatura_media:.2f}°C")
    else:
        print("Não há temperaturas válidas para calcular as estatísticas.")

# Função para o menu
def menu():
    while True:
        print("\nMENU")
        print("1- Consulta de dados por data")
        print("2- Consulta estatística")
        print("3- Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            consultar_por_data()
        elif opcao == '2':
            consultar_estatisticas()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Chama o menu principal
menu()  