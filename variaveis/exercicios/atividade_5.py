DESCONTO_MAXIMO = 0.10
preco_produto = 1350
preco_final = preco_produto - (preco_produto * DESCONTO_MAXIMO)

print("Preço do produto: R$", preco_produto)
print("Desconto máximo:", preco_produto / 10)
print("Preço final: R$", preco_final)