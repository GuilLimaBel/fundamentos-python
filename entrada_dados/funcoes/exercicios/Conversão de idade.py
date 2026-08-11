def converter_idade():
    idade = int(input("Digite sua idade em anos: "))

    meses = idade * 12
    dias = idade * 365

    print("Idade em meses:", meses)
    print("Idade em dias:", dias)

converter_idade()