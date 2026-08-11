def calcular_consumo():
    distancia = float(input("Digite a distância percorrida (km): "))
    combustivel = float(input("Digite a quantidade de combustível (L): "))

    consumo = distancia / combustivel

    print("Consumo médio:", consumo, "km/L")

calcular_consumo()