def heartRate(fc):
    if 50 <= fc <= 80:
        return "treino aerobico"
    elif 80 < fc <= 100:
        return "treino cardiovascular"
    elif 100 < fc <= 120:
        return "treino aerobico ideal"
    elif 120 < fc <= 140:
        return "treino anaerobico"
    else:
        return "frequencia cardiaca fora dos limites"

print(heartRate(56))
print(heartRate(98))
print(heartRate(110))
print(heartRate(135))
print(heartRate(43))