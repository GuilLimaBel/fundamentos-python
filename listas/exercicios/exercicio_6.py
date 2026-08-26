def encontrar_produto(produtos, produto):
    return produtos.index(produto)


produtos = ["Mouse", "Teclado", "Monitor", "Webcam"]

produto = input("Digite o produto que deseja encontrar: ")

if produto in produtos:
    posicao = encontrar_produto(produtos, produto)
    print("O produto está na posição:", posicao)
else:
    print("Produto não encontrado.")