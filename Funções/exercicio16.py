def investimento(valor_inicial, juros, periodo):
    m = valor_inicial * ((1 + juros)**periodo)
    return round(m)

valor_inicial = float(input("Informe o valor inicial: "))
juros = float(input("Informe o valor do juros (10% = 0.1): "))
periodo = int(input("Informe a quantidade de periodos: "))
print("Esse valor resultará em R$",investimento(valor_inicial, juros, periodo))