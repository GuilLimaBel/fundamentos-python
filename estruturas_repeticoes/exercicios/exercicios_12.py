def eh_primo(numero):

    if numero < 2:
        return False

    for contador in range(2, numero):
        if numero % contador == 0:
            return False

    return True


numero = int(input("Digite um número: "))

if eh_primo(numero):
    print("O número é primo!")
else:
    print("O número não é primo!")