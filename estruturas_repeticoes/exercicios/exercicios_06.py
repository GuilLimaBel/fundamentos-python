def somar_ate(numero):
    total = 0

    for contador in range(1, numero + 1):
        total += contador

    return total


numero = int(input("Digite um número: "))

resultado = somar_ate(numero)

print(f"A soma dos números é {resultado}")