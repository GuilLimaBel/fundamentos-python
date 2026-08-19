def contagem_regressiva(numero):
    while numero >= 0:
        print(f"Contagem regressiva: {numero}")
        numero -= 1

    print("DECOLANDO!!!")


numero = int(input("Digite um número: "))

contagem_regressiva(numero)