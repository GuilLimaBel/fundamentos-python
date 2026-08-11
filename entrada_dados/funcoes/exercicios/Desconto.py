def calcular_desconto():
    preco = float(input("Digite o preço do produto: R$ "))
    desconto = float(input("Digite o percentual de desconto: "))

    valor_desconto = preco * desconto / 100
    valor_final = preco - valor_desconto

    print("Valor final: R$", valor_final)

calcular_desconto()