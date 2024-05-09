def media(nota1, peso1, nota2, peso2, nota3, peso3):
    r = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
    return r

nota1 = float(input("Informe a primiera nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
peso1 = float(input("Informe o peso da primiera nota: "))
peso2 = float(input("Informe o peso da segunda nota: "))
peso3 = float(input("Informe o peso da terceira nota: "))
print("A média ponderada dessas notas é",media(nota1, peso1, nota2, peso2, nota3, peso3))