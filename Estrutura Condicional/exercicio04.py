quantidade = int(input("Informe a quantidade de maçãs: "))

if quantidade >= 12:
    preco = 0.25
else:
    preco = 0.30

total = quantidade * preco
print("Você pagará R$", total)