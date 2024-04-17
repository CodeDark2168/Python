data = input("Informe a data (dd/mm/aaaa): ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])
bissexto = ano % 4

if bissexto == 0:
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            print("Data Válida")
        else:
            print("Data Inválida")
    elif mes == 2:
        if dia >= 1 and dia <= 29:
            print("Data Válida")
        else:
            print("Data Inválida")
    else:
        if dia >= 1 and dia <= 31:
            print("Data Válida")
        else:
            print("Data Inválida")
else:
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            print("Data Válida")
        else:
            print("Data Inválida")
    elif mes == 2:
        if dia >= 1 and dia <= 28:
            print("Data Válida")
        else:
            print("Data Inválida")
    else:
        if dia >= 1 and dia <= 31:
            print("Data Válida")
        else:
            print("Data Inválida")



