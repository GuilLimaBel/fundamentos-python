def mostrar_pares(numero):
    for contador in range(1, numero + 1):
        if contador % 2 == 0:
            print(f"Número par = {contador}")


numero = int(input("Digite um número: "))

mostrar_pares(numero)