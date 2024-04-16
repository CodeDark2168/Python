sexo = int(input("Informe seu gênero (1 = feminino 2 = masculino): "))
altura = float(input("Informe sua altura: "))

if sexo == 1:
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal é de", peso_ideal)
elif sexo == 2:
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é de", peso_ideal)
else:
    print("Código Inválido")