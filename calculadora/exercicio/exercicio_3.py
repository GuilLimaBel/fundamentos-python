def adicionar_informacoes():
    pessoa = {
        "nome": "Guilherme",
        "idade": 17
    }

    pessoa["email"] = input("Digite o email: ")
    pessoa["endereco"] = input("Digite o endereço: ")
    pessoa["telefone"] = input("Digite o telefone: ")

    print("\nDADOS CADASTRADOS:")
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    print("Email:", pessoa["email"])
    print("Endereço:", pessoa["endereco"])
    print("Telefone:", pessoa["telefone"])


adicionar_informacoes()