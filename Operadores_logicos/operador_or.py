#Opeerador or

def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input("Voce tem mais dinheiro para comprar? "))
    autrizado = tem_dinheiro or tem_dinheiro or TEM_CARTAO
    print(f"Vou comer um MC-Donalds hoje?  {autrizado} ")

posso_comprar()