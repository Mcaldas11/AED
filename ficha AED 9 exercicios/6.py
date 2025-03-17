nTermos = int(input("Indique um numero de termos da sequencia de Fibonacci: "))

seqTermos = ""

if nTermos < 0 :
    print("Por favor, indique um numero inteiro positivo")


if nTermos >= 1 :
    seqTermos = "0"
if nTermos >= 2 : 
    seqTermos += ", 1"

penultimoTermo = 0
ultimoTermo = 1

for i in range(3, nTermos + 1):
    proximoTermo = penultimoTermo + ultimoTermo
    seqTermos += f",{proximoTermo}"
    penultimoTermo, ultimoTermo = ultimoTermo, proximoTermo

print(f"Os primeiroa {nTermos} da sequencia de Fibonacci sao: {seqTermos}")


