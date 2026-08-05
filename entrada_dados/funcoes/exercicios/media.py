def calcular_media():
    nota1 = float(input("Digite a nota da primeira : "))
    nota2 = float(input("Digite a nota da segunda : "))
    nota3 = float(input("Digite a nota da terceira : "))
    media = (nota1 + nota2 + nota3) / 3
    return media

nota_final = calcular_media()
print(f"A nota final é {nota_final}")