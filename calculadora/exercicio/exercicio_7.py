def verificar_aprovacao():
    aluno = {
        "nome": "Guilherme",
        "idade": 17,
        "cidade": "Piracicaba",
        "media": 7.5,
        "frequencia": 80
    }

    if aluno["media"] >= 6 and aluno["frequencia"] >= 75:
        print(aluno["nome"], "foi aprovado!")
    else:
        print(aluno["nome"], "foi reprovado.")


verificar_aprovacao()