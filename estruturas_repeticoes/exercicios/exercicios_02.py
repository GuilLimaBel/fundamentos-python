def contar_ate(numero):
    for contador in range(1, numero + 1):
        print(f"O número atual é {contador}")


numero = int(input("Digite um número: "))

contar_ate(numero)