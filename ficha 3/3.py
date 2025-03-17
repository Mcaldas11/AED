def capicua(texto):
    texto = texto.replace(" ", "").lower()

    return texto == texto[::-1]

texto = input("Insira um texto: ")
if capicua(texto):
    print(f"O texto {texto} é uma capicua")
else:
    print(f"O texto {texto} não é uma capicua")