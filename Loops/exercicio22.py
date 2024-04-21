valor_1 = int(input("Informe o primeiro valor: "))
valor_2 = int(input("Informe o segundo valor: "))
valor_3 = int(input("Informe o terceiro valor: "))
valor_4 = int(input("Informe o quarto valor: "))
valor_5 = int(input("Informe o quinto valor: "))
valor_6 = int(input("Informe o sexto valor: "))
valor_7 = int(input("Informe o sétimo valor: "))
valor_8 = int(input("Informe o oitavo valor: "))
valor_9 = int(input("Informe o nono valor: "))
valor_10 = int(input("Informe o décimo valor: "))
lista = [valor_1,valor_2,valor_3,valor_4,valor_5,valor_6,valor_7,valor_8,valor_9,valor_10]
par = []
impar = []


for item in lista:
    if item % 2 == 0:
        par.append(item)
    else:
        impar.append(item)

print("Valores pares:",par)
print("Valores ímpares:",impar)