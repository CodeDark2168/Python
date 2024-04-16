valor_1 = float(input("Insira o primeiro valor: "))
valor_2 = float(input("Insira o segundo valor: "))
valor_3 = float(input("Insira o terceiro valor: "))

if valor_1 > valor_2 and valor_1 > valor_3:
    print("O maior valor é", valor_1)
elif valor_2 > valor_1 and valor_2 > valor_3:
    print("O maior valor é", valor_2)
elif valor_3 > valor_1 and valor_3 > valor_2:
    print("O maior valor é", valor_3)
else:
    print("Os valores não podem ser iguais")