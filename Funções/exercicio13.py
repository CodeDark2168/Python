from array import array


def soma_par(array):
    soma = 0
    for i in array:
        if i % 2 == 0:
            soma += i
    return soma

array = [48, 79, 12, 62, 30, 45, 21, 67, 99, 16]
print("A soma dos números pares é",soma_par(array))