a = 0
b = 1
c = 0

for i in range(90):
    c = b
    b = a
    a = b + c
    print(a)

