def remover_telefone():
    funcionario = {
        "nome": "Guilherme",
        "idade": 17,
        "cidade": "Piracicaba",
        "cargo": "Analista",
        "salario": 3500,
        "telefone": "19999999999"
    }

    print("ANTES DA REMOÇÃO:")
    print(funcionario)

    telefone_removido = funcionario.pop("telefone")

    print("\nTELEFONE REMOVIDO:")
    print(telefone_removido)

    print("\nDEPOIS DA REMOÇÃO:")
    print(funcionario)


remover_telefone()