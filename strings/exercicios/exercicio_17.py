def limpar_telefone(telefone):
    telefone = telefone.replace("(", "")
    telefone = telefone.replace(")", "")
    telefone = telefone.replace(" ", "")
    telefone = telefone.replace("-", "")

    return telefone


telefone = input("Digite o telefone no formato (19) 99999-8888: ")

print(limpar_telefone(telefone))