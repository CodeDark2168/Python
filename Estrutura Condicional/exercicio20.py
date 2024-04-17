import random

jogador = input("Escolha pedra, papel ou tesoura: ")
escolhas = ["Pedra","Papel","Tesoura"]
computador = escolhas[random.randint(0,3)]
print("Jogador:",jogador)
print("Computador:",computador)

if jogador == "Pedra" and computador == "Tesoura" or jogador == "Tesoura" and computador == "Papel" or jogador == "Papel" and computador == "Pedra":
    print("O jogador ganhou")
elif jogador == computador:
    print("Houve empate")
else:
    print("O computador ganhou")