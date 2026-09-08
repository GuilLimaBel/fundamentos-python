# Dividir uma string em partes"
def separar_nome(nome_completo):
    partes = nome_completo.split()
    return partes

nome_completo = input("Digite seu nome completo: ")
print(f"Nome em partes: {separar_nome(nome_completo)}")

#Juntar Strings
def criar_nome_completo(partes):
    nome_completo = " ".join(partes)
    return nome_completo
partes_nome = ["João", "Renam", "Celso"]
print(f"A junção das partes do nome é: {criar_nome_completo(partes_nome)}")

#Verificar o inicio e o final de uma string
def analisar_url(url):
    inicia_com_https = url.startswith("https://")
    termina_com_br = url.endwith(".br")
    return inicia_com_https, termina_com_br

url = "https://www.gov.br"
tem_https, tem_br = analisar_url(url)
print(f"Utiliza https? {tem_https}")
print(f"termina em br? {tem_br}")

#Verificar se a strig contém somnte números
def validar_idade(idade):
    idade_valida = idade.isdigit()
    if idade_valida:
        print("O valor digitado é uma idade válida!")
    else:
        print("Digite somente números")

idade = input("Digite sua idade: ")
validar_idade(idade)

#Verificar se a strign contém someente letras
def_validar_nome(nome)
    nome_valido = nome.isalpha(
)