def cadastro_notas():
    aluno = {}

    aluno["nome"] = "Guilherme"
    aluno["idade"] = 17
    aluno["cidade"] = "Piracicaba"

    aluno["nota1"] = float(input("Digite a primeira nota: "))
    aluno["nota2"] = float(input("Digite a segunda nota: "))
    aluno["nota3"] = float(input("Digite a terceira nota: "))

    media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3

    aluno["media"] = media

    print("\nDADOS DO ALUNO:")
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Cidade:", aluno["cidade"])
    print("Nota 1:", aluno["nota1"])
    print("Nota 2:", aluno["nota2"])
    print("Nota 3:", aluno["nota3"])
    print("Média:", aluno["media"])


cadastro_notas()