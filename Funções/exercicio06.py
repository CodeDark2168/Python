def media(array):
    soma = 0
    for i in array:
        soma += i
    media = soma / len(array)
    return media

array = [10, 7, 8.5, 2, 4]
print("A média desses números é",media(array))