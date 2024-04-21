valor_1 = int(input("Informe o primeiro valor: "))
valor_2 = int(input("Informe o segundo valor: "))
valor_3 = int(input("Informe o terceiro valor: "))
valor_4 = int(input("Informe o quarto valor: "))
valor_5 = int(input("Informe o quinto valor: "))
lista = [valor_1,valor_2,valor_3,valor_4,valor_5]
maior = lista[0]

for item in lista:
    if item >= maior:
        maior = item

print("Maior valor: ",maior)
    
