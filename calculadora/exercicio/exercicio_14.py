def aluno_notas():
    aluno = {
        "nome": "Guilherme",
        "idade": 17,
        "cidade": "Piracicaba",
        "notas": [8.0, 7.5, 9.0]
    }

    media = sum(aluno["notas"]) / len(aluno["notas"])

    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Cidade:", aluno["cidade"])
    print("Todas as notas:", aluno["notas"])
    print("Maior nota:", max(aluno["notas"]))
    print("Menor nota:", min(aluno["notas"]))
    print("Média:", media)


aluno_notas()