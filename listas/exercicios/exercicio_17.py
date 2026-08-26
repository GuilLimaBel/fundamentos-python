def vender_produto(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
        print("Produto vendido com sucesso!")
    else:
        print("Produto não está disponível.")

    return estoque


estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

produto = input("Digite o produto que deseja comprar: ")

estoque_atualizado = vender_produto(estoque, produto)

print("Estoque atual:", estoque_atualizado)