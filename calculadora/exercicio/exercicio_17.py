def cadastro_alunos():
    alunos = []

    for i in range(5):
        print("\nCADASTRO DO ALUNO", i + 1)

        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        nota = float(input("Digite a nota: "))

        aluno = {
            "nome": nome,
            "idade": idade,
            "nota": nota,
            "cidade": "Piracicaba"
        }

        alunos.append(aluno)

    print("\nDADOS DE TODOS OS ALUNOS:")

    for aluno in alunos:
        print("Nome:", aluno["nome"])
        print("Idade:", aluno["idade"])
        print("Nota:", aluno["nota"])
        print("Cidade:", aluno["cidade"])
        print("--------------------")


cadastro_alunos()