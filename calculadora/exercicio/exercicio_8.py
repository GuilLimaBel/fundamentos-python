def sistema_login():
    usuario = {
        "login": "guilherme",
        "senha": "1234"
    }

    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == usuario["login"] and senha == usuario["senha"]:
        print("Login realizado com sucesso!")
    else:
        print("Login ou senha incorretos.")


sistema_login()