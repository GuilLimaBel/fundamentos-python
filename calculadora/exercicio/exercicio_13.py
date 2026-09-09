def limpar_cadastro():
    funcionario = {
        "nome": "Guilherme",
        "idade": 17,
        "cidade": "Piracicaba",
        "cargo": "Analista",
        "salario": 3500,
        "telefone": "19999999999"
    }

    chave = input("Digite a chave que deseja remover: ")

    if chave in funcionario:
        del funcionario[chave]
        print("Chave removida com sucesso!")
    else:
        print("Essa chave não existe.")

    print("\nDICIONÁRIO ATUALIZADO:")
    print(funcionario)


limpar_cadastro()