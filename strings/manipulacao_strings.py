# Converter texto para maiúsculas e minúsculas
def formatar_nome(nome):
    nome_maisculo = nome.upper()
    nome_minusculo = nome.lower()

    # Nome com primeira letra maiúscula
    nome_camel_case = nome.capitalize()

    return nome_maisculo, nome_minusculo, nome_camel_case


nome = input("Digite seu nome: ")

banana, batata, cebola = formatar_nome(nome)

print(f"Nome maiúsculo: {banana}")
print(f"Nome minúsculo: {batata}")
print(f"Nome camel case: {cebola}")


# Remover espaços desnecessários
def limpar_texto(texto):
    # Remove espaços no início e no final do texto
    texto_limpo = texto.strip()

    return texto_limpo


texto_1 = "     Aprender Python é legal!!       "

print(f"Texto antes: {texto_1}")
print(f"Texto depois: {limpar_texto(texto_1)}")


# Substituir palavras
def trocar_cidade(texto, cidade):
    # Troca uma palavra por outra
    texto_trocado = texto.replace(cidade, "Piracicaba")

    return texto_trocado


cidade = input("Digite a cidade que você mora: ")
texto_cidade = f"Eu moro em {cidade}."

print(trocar_cidade(texto_cidade, cidade))


# Contar caracteres ou ocorrências
def analisar_texto(texto, letra):
    # Contar a quantidade de caracteres
    qtde_caracteres = len(texto)

    # Contar a quantidade de ocorrências da letra A
    qtd_letra_a = texto.strip().lower().count(letra)

    return qtd_caracteres, qtde_letra

texto_2 = input("Digite seu texto: ")
letra = input("Digite uma letra: ")
caracteres, letras = analisar_texto(texto_2, letra)

print(f"Total de caracteres: {caracteres}")
print(f"Total de letras : {letras}")

#Verificar se uma palavra stá presente
def verificar_palavra(frase, palavra):
    palavras_presenete = palavra.lower() in frase.lower()
    return palavras_presenete
frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

print(f"A palavra está presente: {verificar_palavra(frase, palavra)}")

#  Encontrar a posição de uma palavra
def encontrar_posicao_palavra(frase, palavra):
    posicao_palavra = frase.lower().find(palavra.loweer())
    return posicao_palavra
frase_2 = input("Digite uma nova frase: ")
palavra_2 = input("Digite uma palavra para saber sua posição: ")

print(f"")