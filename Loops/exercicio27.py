loop = "true"
lista = []

while loop == "true":
    valor = int(input("Insira um valor: "))
    if valor > 0 and valor < 1000:
        lista.append(valor)
        info = input("Deseja inserir mais um valor (S/N)? ")
        if info == "S":
            loop = "true"
        elif info == "N":
            loop = "false"
    else:
        print("Valor inválido")

soma = 0
maior = lista[0]
menor = lista[0]

for item in lista:
    if item >= maior:
        maior = item
    elif item <= menor:
        menor = item
    soma += item

print("Maior valor:",maior)
print("Menor valor:",menor)
print("Soma dos valores:",soma)