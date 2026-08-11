def calcular_imc():
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    imc = peso / (altura ** 2)

    print("IMC:", imc)

calcular_imc()