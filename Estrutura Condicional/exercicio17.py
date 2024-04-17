idade = int(input("Informe sua idade: "))
cnh = input("Você possui CNH? ")

if idade >= 18 and cnh == "Sim":
    print("Você pode dirigir")
else:
    print("Você não pode dirigir")