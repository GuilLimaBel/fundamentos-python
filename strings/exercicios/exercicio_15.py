def validar_especie(animal):
    if animal.isalpha():
        return "Espécie de animal válida."
    else:
        return "Espécie inválida."


animal = input("Digite uma espécie de animal: ")

print(validar_especie(animal))