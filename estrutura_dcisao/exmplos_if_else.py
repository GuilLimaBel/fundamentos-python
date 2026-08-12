def aluno_apropriado():
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))

    media = (nota_1 + nota_2) / 2

    if media >= 6:
        print("Aluno aprovado!")
    elif media >= 5 and media < 6:
        print("Aluno de recuperação!")
    else:
        print("Aluno reprovado!")

aluno_apropriado()




def login():
    e_mail = "guilherme@b"
    senha = "1234"
    codigo_secreto = "456@"

    email_input= input("Digite seu e-mail: ")
    senha_input= input("Digite sua senha: ")

    if email_input == e_mail and senha_input == senha:
        print("Úsuario Logado!")
        acessar_admin = input("Deseja acessar area administrativa?(Digite S ou N: ")
        if acessar_admin == "S" and "s":
            codigo_secreto = input("Digite seu codigo secreto: ")
            if codigo_secreto == codigo_secreto:
                print("Acesso adm Liberado!")
            else:
                print("Codgio errado!")

        elif acessar_admin == "N" and "n":
            print("Ok. Você acessou como úsuario comum!")
        else:
            print("Opção invalida!")

    else:
        print("E-mail ou senha incorreto!")

login()