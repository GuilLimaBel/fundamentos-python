def calcular_media():

    total = 0
    quantidade = 0

    while True:

        numero = float(input("Digite um número (0 para parar): "))

        if numero == 0:
            break

        total += numero
        quantidade += 1

    if quantidade > 0:
        media = total / quantidade
        print(f"A média dos números é: {media}")

    else:
        print("Nenhum número foi informado.")


calcular_media()