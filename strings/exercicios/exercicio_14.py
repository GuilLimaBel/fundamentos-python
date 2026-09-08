def validar_telefone(numeros):
    if numeros.isdigit():
        return "Número de telefone válido!"
    else:
        return "Número inválido! Digite somente números."


numeros = input("Digite o número de telefone: ")

print(validar_telefone(numeros))