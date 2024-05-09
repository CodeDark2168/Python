def conversao(hora, minuto, segundo):
    segundo = (hora * 360) + (minuto * 60) + segundo
    return segundo

hora = int(input("Informe aa horas: "))
minuto = int(input("Informe os minutos: "))
segundo = int(input("Informe os segundos: "))
print("Essa hora corresponde a",conversao(hora, minuto, segundo),"segundos")
