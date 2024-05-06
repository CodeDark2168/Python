def soma(n1):
    soma = 0
    for i in n1:
        soma += int(i)
    return soma

n1 = input("Informe um número: ")
print("A soma dos dígitos é",soma(n1))