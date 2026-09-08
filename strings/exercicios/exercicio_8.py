def verificar_palavra(texto, palavra):
    if palavra in texto:
        return "Palavra encontrada!"
    else:
        return "Palavra não encontrada!"


texto = input("Digite um texto: ")
palavra = input("Digite a palavra que deseja verificar: ")

print(verificar_palavra(texto, palavra))