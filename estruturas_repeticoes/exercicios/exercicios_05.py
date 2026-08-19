def tabuada(numero):
    for contador in range(1, 11):
        resultado = numero * contador
        print(f"{numero} x {contador} = {resultado}")


numero = int(input("Digite um número: "))

tabuada(numero)