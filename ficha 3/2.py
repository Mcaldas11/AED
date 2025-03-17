def countText(texto):
    caracteres = len(texto)
    
    espacos = texto.count(' ')
    
    vogais = 'aeiouAEIOU'
    numVogais = sum(1 for char in texto if char in vogais)

    print(f"Nº caracteres: {caracteres}")
    print(f"Nº espacos: {espacos}")
    print(f"Nº vogais: {numVogais}")

texto_input = input("Indique um texto: ")
countText(texto_input)