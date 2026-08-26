def adicionar_cliente(fila, cliente):
    fila.append(cliente)


def atender_cliente(fila):
    return fila.pop(0)


fila = []

while True:
    cliente = input("Digite o nome do cliente ou 'sair' para encerrar: ")

    if cliente.lower() == "sair":
        break

    adicionar_cliente(fila, cliente)


print("Fila de clientes:", fila)

if len(fila) > 0:
    atendido = atender_cliente(fila)

    print("Cliente atendido:", atendido)
    print("Fila atual:", fila)
else:
    print("Não há clientes na fila.")