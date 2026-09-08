def criar_email(nome, sobrenome, dominio):
    return nome.lower() + "." + sobrenome.lower() + "@" + dominio.lower()


nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
dominio = input("Digite o domínio: ")

print(criar_email(nome, sobrenome, dominio))