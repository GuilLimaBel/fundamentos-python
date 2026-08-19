def menu():

    while True:

        print("\n===== MENU =====")
        print("1 - Exibir números de 1 a 10")
        print("2 - Exibir números pares")
        print("3 - Exibir tabuada")
        print("4 - Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":

            for numero in range(1, 11):
                print(f"Número atual: {numero}")

        elif opcao == "2":

            numero = int(input("Digite até qual número: "))

            for contador in range(1, numero + 1):

                if contador % 2 == 0:
                    print(f"Número par: {contador}")

        elif opcao == "3":

            numero = int(input("Digite um número: "))

            for contador in range(1, 11):
                print(f"{numero} x {contador} = {numero * contador}")

        elif opcao == "4":

            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")


menu()