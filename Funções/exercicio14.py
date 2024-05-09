def fibonacci(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        a = b + c
        c = b
        b = a
    return a

n = int(input("Informe qual termo deseja: "))
print(fibonacci(n))