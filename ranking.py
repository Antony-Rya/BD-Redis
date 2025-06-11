from utilidade import limpar_terminal

class Ranking:
    def __init__(self, r):
        self.redis = r
        self.key = 'pontuacoes'

    def adicionarAtualizarJogador(self, nome: str, pontuacao: int):
        self.redis.zadd(self.key, {nome: pontuacao})
        print(nome, ' - ',  pontuacao)

    def top_5(self):
        ranking_top5 = self.redis.zrevrange(self.key, 0, 4, withscores=True)
        for i, (nome, pontuacao) in enumerate(ranking_top5, start=1):
            print(f"{i}. {nome} - {pontuacao}")



menu = True
def rankingmenu(ranking):
    global menu
    while menu:
        limpar_terminal()
        print('################')
        print('1 - Adicionar/Atualizar pontuação')
        print('2 - Mostrar Top 5')
        print('3 - Sair')
        print('#################')
        opcao = input('Digite sua opção... ')
        match opcao:
            case '1':
                nome = input("Digite o nome do jogador: ")
                pontuacao = int(input("Digite a pontuação: "))
                ranking.adicionarAtualizarJogador(nome.decode('utf-8'), pontuacao)
            case '2':
                ranking.top_5()
            case '3':
                print('Saindo...')
                menu = False
            case _:
                print("Opção inválida")

