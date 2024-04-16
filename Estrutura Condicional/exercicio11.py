angulo_1 = int(input("Insira o valor do primeiro ângulo: "))
angulo_2 = int(input("Insira o valor do segundo ângulo: "))
angulo_3 = int(input("Insira o valor do terceiro ângulo: "))

if angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90:
    print("Triângulo Retângulo")
elif angulo_1 >= 90 or angulo_2 >= 90 or angulo_3 >= 90:
    print("Triângulo Obtusângulo")
else:
    print("Triângulo Acutângulo")