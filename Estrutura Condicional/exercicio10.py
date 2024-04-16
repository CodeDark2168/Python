lado_1 = float(input("Insira o valor do primeiro lado: "))
lado_2 = float(input("Insira o valor do segundo lado: "))
lado_3 = float(input("Insira o valor do terceiro lado: "))

if lado_1 == lado_2 and lado_2 == lado_3:
    print("Triângulo Equilátero")
elif lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3:
    print("Triângulo Escaleno")
else:
    print("Triângulo Isósceles")