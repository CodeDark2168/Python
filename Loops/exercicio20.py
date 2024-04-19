valor_1 = int(input("Informe o primeiro valor: "))
valor_2 = int(input("Informe o segundo valor: "))
lista = []
soma = 0

for i in range(valor_1,valor_2 + 1,1):
    lista.append(i)
    soma += i

print(lista)
print(soma)