def caixa_eletronico(valor):

    notas = [100, 50, 20, 10, 5, 2]

    for nota in notas:

        quantidade = valor // nota

        if quantidade > 0:
            print(f"Notas de R$ {nota}: {quantidade}")

        valor = valor % nota


valor = int(input("Digite o valor para sacar: "))

caixa_eletronico(valor)