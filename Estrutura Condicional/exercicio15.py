ano = int(input("Insira o ano: "))
bissexto = ano % 4

if bissexto == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
