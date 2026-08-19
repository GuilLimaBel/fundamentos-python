def somar_pares(inicio, fim):
    total = 0

    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            total += numero

    return total


inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

resultado = somar_pares(inicio, fim)

print(f"A soma dos números pares é: {resultado}")