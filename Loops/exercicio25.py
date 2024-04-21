valor = int(input("Informe um valor: "))
fatorial = 1

for i in range(1,valor + 1):
    fatorial *= i

print("Seu fatorial é",fatorial)