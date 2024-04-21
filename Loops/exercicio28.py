loop = "true"

while loop == "true":
    valor = int(input("Insira um valor: "))
    if valor > 0 and valor < 16:
        fatorial = 1

        for i in range(1,valor + 1):
            fatorial *= i

        print("Seu fatorial é",fatorial)
        info = input("Deseja inserir mais um valor (S/N)? ")

        if info == "S":
            loop = "true"
        elif info == "N":
            loop = "false"
    else:
        print("Valor inválido")