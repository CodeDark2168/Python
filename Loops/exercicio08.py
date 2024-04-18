quant = int(input("Quantos números deseja inserir na lista? "))
lista = []

for i in range(quant):
    item = int(input("Insira o valor: "))
    lista.append(item)

for i in lista:
    print(i)