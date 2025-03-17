import random

def inicializar_matriz(dim):
    matriz = [[random.randint(10, 100) for _ in range(dim)] for _ in range(dim)]
    imprimir_matriz(matriz)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" | ".join(map(str, linha)))

def matriz_transposta(matriz):
    transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    print("\nMatriz Transposta:")
    imprimir_matriz(transposta)

def maior_valor(matriz):
    maior = max(max(linha) for linha in matriz)
    print(f"\nMaior valor na matriz: {maior}")

def main():
    while True:
        print("\nMenu:")
        print("1. Inicializar matriz")
        print("2. Matriz transposta")
        print("3. Maior valor")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            dim = int(input("Digite a dimensão da matriz (nº de linhas e colunas): "))
            matriz = inicializar_matriz(dim)
        elif opcao == '2':
            if 'matriz' in locals():
                matriz_transposta(matriz)
            else:
                print("Primeiro, inicialize a matriz.")
        elif opcao == '3':
            if 'matriz' in locals():
                maior_valor(matriz)
            else:
                print("Primeiro, inicialize a matriz.")
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()