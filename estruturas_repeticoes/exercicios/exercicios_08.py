def mostrar_multiplos(numero):
    for contador in range(1, 11):
        resultado = numero * contador
        print(f"Múltiplo: {resultado}")


numero = int(input("Digite um número: "))

mostrar_multiplos(numero)