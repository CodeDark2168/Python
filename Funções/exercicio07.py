def primo(n1):
    r = "é um número primo"
    if n1 == 2:
        r = "não é um número primo"
    for i in range(2,n1):
        if n1 % i == 0:
            r = "não é um número primo"
    return r

n1 = int(input("Informe um número: "))
print("Esse número",primo(n1))