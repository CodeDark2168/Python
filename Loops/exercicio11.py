nota = int(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    nota = int(input("Nota inválida, por favor digite novamenter: "))