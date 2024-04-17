palavra = input("Digite uma palavra: ")
invertido = palavra[::-1]

if invertido == palavra:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")