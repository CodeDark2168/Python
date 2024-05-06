def palindromo(string):
    string_invert = string[::-1]
    if string_invert == string:
        r = "é um palíndromo"
    else:
        r = "não é um palíndromo"
    return r

string = input("Informe uma palavra: ")
print("Essa palavra",palindromo(string))