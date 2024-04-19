usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

while usuario == senha:
    print("Usuário não pode ser igual a senha!")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")