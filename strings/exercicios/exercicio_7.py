def procurar_palavra(texto, palavra):
    posicao = texto.find(palavra)

    if posicao == -1:
        return "A palavra não existe no texto."
    else:
        return f"A palavra começa na posição {posicao}."


texto = input("Digite um texto: ")
palavra = input("Digite a palavra que deseja procurar: ")

print(procurar_palavra(texto, palavra))