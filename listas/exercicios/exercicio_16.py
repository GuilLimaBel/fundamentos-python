def criar_ranking(pontuacoes):
    return sorted(pontuacoes, reverse=True)


pontuacoes = [150, 300, 90, 450, 200]

ranking = criar_ranking(pontuacoes)

print("Ranking:", ranking)