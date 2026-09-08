def verificar_extensao(nome_arquivo):
    if nome_arquivo.endswith(".pdf"):
        return "Arquivo válido."
    else:
        return "Arquivo inválido."


nome_arquivo = input("Digite o nome do arquivo: ")

print(verificar_extensao(nome_arquivo))