def vogais(string):
    vogais = 0
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vogais += 1
    return vogais

string = input("Informe uma palavra: ")
print("Essa palavra tem",vogais(string),"vogais")