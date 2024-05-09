import string


def pangrama(string):
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in string:
        for letra in alfabeto:
            if i == letra:
                alfabeto.remove(letra)
    if alfabeto == []:
        r = "é pangrama"
    else:
        r = "não é pangrama"
    return r

string = input("Informe uma frase: ")
print("A frase inserida",pangrama(string))