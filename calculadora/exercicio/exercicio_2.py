def alterar_informacoes():
    aluno = {
        "nome": "Guilherme",
        "idade": 17,
        "telefone": "19988888888",
        "endereco": "Rua Central, 50",
        "cidade": "Piracicaba",
        "nota": 8.5,
        "turma": "ADS 1",
        "curso": "Desenvolvimento de Sistemas"
    }

    print("ANTES DAS ALTERAÇÕES:")
    print(aluno)

    aluno["idade"] = 18
    aluno["cidade"] = "Campinas"

    print("\nDEPOIS DAS ALTERAÇÕES:")
    print(aluno)


alterar_informacoes()