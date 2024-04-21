valor = int(input("Informe um valor: "))
primo = "true"

if valor != 2:
    for i in range(2,valor):
        if valor % i == 0:
            primo = "false"

if primo == "true":
    print("É um número primo")
else:
    print("Não é um número primo")

