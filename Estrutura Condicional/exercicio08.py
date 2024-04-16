import math

lado = int(input("Informe o número de lados: "))
medida = float(input("Informe o tamanho dos lados: "))

if lado == 3:
    area = (math.sqrt(3)/4) * medida**2
    print("Triângulo com area de ", round(area, 2))
elif lado == 4:
    area = lado**2
    print("Quadrado com area de ", round(area, 2))
elif lado == 5:
    area = (1/4) * math.sqrt(5 * (5 + (2 * math.sqrt(5))) * lado**2)
    print("Pentágono com area de ", round(area, 2))
elif lado < 3:
    print("Não é um polígono")
else:
    print("Polígono não identificado")