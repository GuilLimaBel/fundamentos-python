def remover_item(itens, posicao):
    return itens.pop(posicao)

itens = ["Mouse", "Teclado", "Monitor", "Webcam"]

posicao = int(input("Digite a posição que deseja remover: "))

removido = remover_item(itens, posicao)

print("Item removido:", removido)
print("Lista atual:", itens)