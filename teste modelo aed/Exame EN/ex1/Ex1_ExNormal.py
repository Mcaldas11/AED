#Numero: 40240221
#Nome: Miguel Menicio Caldas

#Matriculas autorizdas a entrar no parque
gessList = ['00-CC-00', '01-CC-01', '02-CC-02', '03-CC-03', '04-CC-04','05-CC-05', '06-CC-06', '07-CC-07', '08-CC-08', '09-CC-09']
#lista que gere a ocupação do parque
parkList = []

def parkValidator(matricula, movimento):
    if movimento == 'E':  #permite a entrada
        return matricula in gessList and matricula not in parkList
    elif movimento == 'S':  #permite a saída
        return matricula in parkList
    return False  #Movimento inválido

def parkManager(matricula, movimento):
    if movimento == 'E':
        parkList.append(matricula)  #Adiciona a matrícula ao parque
    elif movimento == 'S':
        parkList.remove(matricula)  #Remove a matrícula do parque

def main():
    print("Bem-vindo ao sistema de estacionamento da ESMAD")
    print("Digite a sua matrícula seguida de 'E' para entrada ou 'S' para saída.")
    print("Digite '00-00-00' para encerrar o programa.")

    total_veiculos = 0  

    while True:
        movimento = input("Insira a matrícula e o tipo de movimento (Ex: 00-CC-00E ou 00-CC-00S): ").strip()

        if movimento == '00-00-00':  #Termina o programa
            break

        if len(movimento) < 2:  #valida a entrada 
            print("Entrada inválida. Tente novamente.")
            continue

        matricula = movimento[:-1]
        tipo = movimento[-1].upper()

        if tipo not in ['E', 'S']:  #Verifica o tipo de movimento
            print("Tipo de movimento inválido. Use 'E' para entrada ou 'S' para saída.")
            continue

        if parkValidator(matricula, tipo):
            parkManager(matricula, tipo)
            total_veiculos += 1 if tipo == 'E' else 0
            acao = "entrou no" if tipo == 'E' else "saiu do"
            print(f"Veículo {matricula} {acao} parque.")
        else:
            print(f"O veículo {matricula} já realizou esse movimento.")

    print(f"O programa foi encerrado. Total de veículos que entraram no parque: {total_veiculos}")

if __name__ == "__main__":
    main()
