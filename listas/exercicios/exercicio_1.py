def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)


lista_de_nomes = ["Guilherme", "Lara", "Ferraz"]

novo_nome = input("Digite um novo nome: ")

adicionar_nome(lista_de_nomes, novo_nome)