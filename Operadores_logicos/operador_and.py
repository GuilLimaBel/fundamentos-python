#Operador and

def pode_dirigir():
    idade = int(input("Digite a idade: "))
    TEM_HABILITAÇÃO = True

    autorizado = idade>= 18 and TEM_HABILITAÇÃO

    print(f"Usuário pode dirigir? {autorizado}")

pode_dirigir()
