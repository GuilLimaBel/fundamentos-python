def calcular_parcela():
    valor = float(input("Digite o valor do produto: R$ "))
    parcelas = int(input("Digite a quantidade de parcelas: "))

    valor_parcela = valor / parcelas

    print("Valor de cada parcela: R$", valor_parcela)

calcular_parcela()