def trocar_valores():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))

    print("\nAntes:")
    print("A =", A)
    print("B =", B)

    A, B = B, A

    print("\nDepois:")
    print("A =", A)
    print("B =", B)

trocar_valores()
