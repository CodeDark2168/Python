valor = int(input("Informe um valor: "))
primo = "true"
divisor = []

if valor != 2:
    for i in range(2,valor):
        if valor % i == 0:
            primo = "false"
            divisor.append(i)

if primo == "true":
    print("É um número primo")
else:
    print("Não é um número primo pois pode ser dividido por:",divisor)