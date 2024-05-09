def bissexto(ano):
    if ano % 4 == 0:
        r = "O ano é bissexto"
    else:
        r = "O ano não é bissexto"
    return r

ano = int(input("Informe o ano: "))
print(bissexto(ano))