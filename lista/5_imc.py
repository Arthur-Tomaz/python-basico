def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


# Programa principal
peso = 56
altura = 1.65

imc = calcular_imc(peso, altura)

print("IMC:", round(imc, 2))

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")