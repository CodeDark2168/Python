def fatorial(n1):
    r = n1
    for i in range(1,n1):
        r *= i
    return r

n1 = int(input("Informe um valor: "))
print("O fatorial é",fatorial(n1))