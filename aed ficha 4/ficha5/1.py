def invert(lista):
    for i in range(3):
        lista.append([])
        for j in range(3):
            lista[i].append(int(input("Introduza um valor: ")))

    print("Matriz Original:\n")
    for i in range(3):
        for j in range(3):
            print(lista[i][j],end=" ")
        print()
    print("\n")

    print("Matriz Transposta:\n")
    for i in range(3):
        for j in range(3):
            print(lista[j][i],end=" ")
        print()


lista = []

invert(lista)