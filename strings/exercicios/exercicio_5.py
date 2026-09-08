def substituir_palavra(frase, palavra_1, palavra_2):
    return frase.replace(palavra_1, palavra_2)


frase = input("Digite uma frase: ")
palavra_1 = input("Digite a palavra antiga: ")
palavra_2 = input("Digite a palavra nova: ")

print(substituir_palavra(frase, palavra_1, palavra_2))