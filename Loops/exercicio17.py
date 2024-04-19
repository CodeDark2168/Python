valor_1 = int(input("Informe o primeiro valor: "))
valor_2 = int(input("Informe o segundo valor: "))
valor_3 = int(input("Informe o terceiro valor: "))
valor_4 = int(input("Informe o quarto valor: "))
valor_5 = int(input("Informe o quinto valor: "))
lista = [valor_1,valor_2,valor_3,valor_4,valor_5]
n = 1

for item in lista:
    for n in range(len(lista)):
        if item > lista[n]:
            maior = item

print("Maior valor: ",maior)
    
