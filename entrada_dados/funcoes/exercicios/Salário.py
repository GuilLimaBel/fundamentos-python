def calcule_salario():
    horas = float(input("Quantas horas você trabalhou?: "))
    valor = float(input("Qual o valor da hora: "))
    salario = horas * valor
    return salario

nota_final = calcule_salario()
print(f"O seu salário diário {nota_final}")