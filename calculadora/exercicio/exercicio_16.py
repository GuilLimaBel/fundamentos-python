def lista_compras():
    compra = {
        "cliente": "Guilherme",
        "idade": 17,
        "cidade": "Piracicaba",
        "produtos": []
    }

    for i in range(5):
        produto = input("Digite o nome do produto: ")
        compra["produtos"].append(produto)

    print("\nCLIENTE:", compra["cliente"])
    print("Idade:", compra["idade"])
    print("Cidade:", compra["cidade"])
    print("PRODUTOS COMPRADOS:")

    for produto in compra["produtos"]:
        print("-", produto)


lista_compras()