def ocorrencias(caracter, string):
    r = string.count(caracter)
    return r

string = input("Informe uma string: ")
caracter = input("Informe o caracter que você deseja verificar: ")
print("Essa string possui",ocorrencias(caracter, string),"letras",caracter)