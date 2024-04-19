a = int(input("Digite o valor da população A: "))
b = int(input("Digite o valor da população B: "))
crescimento_a = float(input("Informe a taxa de crescimento do A: "))
crescimento_b = float(input("Informe a taxa de crescimento do B: "))

crescimento_a /= 100
crescimento_b /= 100
crescimento_a += 1
crescimento_b += 1 

while a < b:
    a *= crescimento_a
    b *= crescimento_b

print("População A:",round(a))
print("População B:",round(b))