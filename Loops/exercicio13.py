nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Digite seu sexo (M ou F): ")
estado_civil = input("Digite seu estado civil (S, C, V ou D): ")

while len(nome) < 3 or idade < 0 or idade > 150 or salario < 0 or sexo != "M" and sexo != "F" or estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D":
    print("Informações inválidas")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))
    sexo = input("Digite seu sexo (M ou F): ")
    estado_civil = input("Digite seu estado civil (S, C, V ou D): ")