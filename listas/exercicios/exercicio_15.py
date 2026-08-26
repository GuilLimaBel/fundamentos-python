def adicionar_nota(notas, nota):
    notas.append(nota)


def remover_nota(notas, nota):
    notas.remove(nota)


def media_notas(notas):
    return sum(notas) / len(notas)


notas = [7.0, 8.5, 6.0]

nova_nota = float(input("Digite uma nova nota: "))

adicionar_nota(notas, nova_nota)

print("Notas:", notas)

nota_remover = float(input("Digite a nota que deseja remover: "))

if nota_remover in notas:
    remover_nota(notas, nota_remover)

print("Notas atualizadas:", notas)

print("Média:", media_notas(notas))