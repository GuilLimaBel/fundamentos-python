def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print(convidados)


convidados = ["Ana", "João"]

novos_convidados = ["Carlos", "Maria", "Pedro"]

adicionar_convidados(convidados, novos_convidados)