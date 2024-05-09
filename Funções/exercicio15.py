from array import array


def crescente(array):
    array.sort()
    return array

array = [12, 54, -71, 61, -42, 91, 3]
print(crescente(array))