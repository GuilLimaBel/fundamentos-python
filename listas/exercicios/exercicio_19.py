def adicionar_nota(notas, nota):
    notas.append(nota)


def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)


def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)


def remover_nota(notas, nota):
    notas.remove(nota)


def remover_ultima_nota(notas):
    return notas.pop()


def encontrar_nota(notas, nota):
    return notas.index(nota)


def quantidade_notas(notas):
    return len(notas)


def ordenar_notas(notas):
    return sorted(notas)


def inverter_notas(notas):
    return list(reversed(notas))


def somar_notas(notas):
    return sum(notas)


def calcular_media(notas):
    return sum(notas) / len(notas)


notas = [7.5, 6.0, 8.5, 9.0, 5.5]

adicionar_nota(notas, 8.0)
print(notas)

inserir_nota(notas, 7.0, 2)
print(notas)

novas_notas = [6.5, 9.5]
adicionar_varias_notas(notas, novas_notas)
print(notas)

remover_nota(notas, 5.5)
print(notas)

ultima = remover_ultima_nota(notas)
print("Nota removida:", ultima)
print(notas)

posicao = encontrar_nota(notas, 8.5)
print("Posição da nota 8.5:", posicao)

print("Quantidade de notas:", quantidade_notas(notas))

print("Notas ordenadas:", ordenar_notas(notas))

print("Notas invertidas:", inverter_notas(notas))

print("Soma das notas:", somar_notas(notas))

print("Média da turma:", calcular_media(notas))