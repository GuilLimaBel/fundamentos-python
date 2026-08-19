def mostrar_impares(numero):
    for contador in range(1, numero + 1):
        if contador % 2 != 0:
            print(f"Número ímpar = {contador}")


numero = int(input("Digite um número: "))

mostrar_impares(numero)