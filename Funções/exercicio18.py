from itertools import count
import string


def palavras(string):
    r = string.count(" ") + 1
    return r

string = input("Informe uma string: ")
print(palavras(string))