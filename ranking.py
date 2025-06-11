class Ranking:
    def __init__(self, r):
        self.redis = r
        self.key = 'pontuacoes'

    def adicionarAtualizarJogador(self, nome: str, pontuacao: int):
        self.redis.zadd(self.key, {nome: pontuacao})
        print(nome, ' ',  pontuacao)

    def top_5(self):
        ranking_top5 = self.redis.zrevrange(self.key, 0, 4, withscores=True)
        for i, (nome, pontuacao) in enumerate(ranking_top5, start=1):
            print(f"{i}. {nome} - {pontuacao}")