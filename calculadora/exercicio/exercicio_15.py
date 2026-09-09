def cadastro_filmes():
    filme = {
        "titulo": "Interestelar",
        "ano": 2014,
        "genero": "Ficção científica",
        "notas": []
    }

    for i in range(5):
        nota = float(input("Digite uma nota para o filme: "))
        filme["notas"].append(nota)

    media = sum(filme["notas"]) / len(filme["notas"])

    print("\nDADOS DO FILME:")
    print("Título:", filme["titulo"])
    print("Ano:", filme["ano"])
    print("Gênero:", filme["genero"])
    print("Notas:", filme["notas"])
    print("Média:", media)


cadastro_filmes()