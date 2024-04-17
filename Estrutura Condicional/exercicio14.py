valor = float(input("Insira o valor: "))
resto_5 = valor % 5
resto_7 = valor % 7

if resto_5 == 0 and resto_7 == 0:
    print("O valor é múltiplo de 5 e de 7")
else:
    print("O valor não é múltiplo de 5 e de 7 ao mesmo tempo")