def fatorial(numero):
    resultado = 1

    for contador in range(1, numero + 1):
        resultado *= contador

    return resultado


numero = int(input("Digite um número: "))

resultado = fatorial(numero)

print(f"O fatorial de {numero} é {resultado}")