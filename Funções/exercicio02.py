def maior(n1,n2,n3):
    array = [n1,n2,n3]
    maior = 0
    for i in array:
        if i > maior:
            maior = i
    return maior

n1 = float(input("Informe o primeiro valor: "))
n2 = float(input("Informe o primeiro valor: "))
n3 = float(input("Informe o primeiro valor: "))
print("O maior deles é",maior(n1,n2,n3))