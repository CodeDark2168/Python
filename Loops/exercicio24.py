a = 0
b = 1
c = 0

while a <= 500:
    c = b
    b = a
    a = b + c
    print(a)