def calcular_salario():
    salario_fixo = float(input("Digite o salário fixo: R$ "))
    vendas = float(input("Digite o valor das vendas: R$ "))
    comissao = float(input("Digite o percentual de comissão: "))

    valor_comissao = vendas * comissao / 100
    salario_final = salario_fixo + valor_comissao

    print("Salário final: R$", salario_final)

calcular_salario()