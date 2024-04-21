base = int(input("Informe o valor da base: "))
expoente = int(input("Informe o valor do expoente: "))
calculo = 1

for i in range(expoente):
    calculo *= base

print("O resultado da potência é",calculo)