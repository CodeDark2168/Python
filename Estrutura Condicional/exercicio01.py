valor_1 = float(input("Insira o primeiro valor: "))
valor_2 = float(input("Insira o segundo valor: "))

if valor_1 > valor_2:
    print("O maior valor é", valor_1)
elif valor_2 > valor_1:
    print("O maior valor é", valor_2)
else:
    print("Os valores são iguais")