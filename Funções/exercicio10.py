def fahrenheit(celcius):
    r = (celcius * 9/5) + 32
    return r

celcius = int(input("Informe a temperatua em celcius: "))
print("Essa temperatura equivale a",fahrenheit(celcius),"F")