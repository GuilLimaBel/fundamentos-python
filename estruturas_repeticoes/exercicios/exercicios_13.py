def mostrar_primos(inicio, fim):

    for numero in range(inicio, fim + 1):

        if numero < 2:
            continue

        primo = True

        for contador in range(2, numero):
            if numero % contador == 0:
                primo = False
                break

        if primo:
            print(f"Número primo: {numero}")


inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

mostrar_primos(inicio, fim)