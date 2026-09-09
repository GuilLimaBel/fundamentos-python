def consultar_cliente():
    cliente = {
        "nome": "Guilherme",
        "idade": 17,
        "email": "guilherme@email.com",
        "cidade": "Piracicaba"
    }

    informacao = input("Digite o nome da informação: ")

    resultado = cliente.get(informacao)

    if resultado is not None:
        print("Informação:", resultado)
    else:
        print("Informação não encontrada.")


consultar_cliente()