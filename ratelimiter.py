from utilidade import limpar_terminal_com_atraso

class RateLimiter:
    def __init__(self, r, limite=3, periodo=60):
        self.redis = r
        self.limite = limite
        self.periodo = periodo

    def permitir_requisicao(self, user_id):
        chave = f"rate_limit:{user_id}"
        requisicoes = self.redis.incr(chave)
        if requisicoes == 1:
            self.redis.expire(chave, self.periodo)
        if requisicoes > self.limite:
            return False
        else:
            return True

    def tempo_restante(self, user_id):
        chave = f"rate_limit:{user_id}"
        return self.redis.ttl(chave)

def ratelimitermenu(limiter):
    menu = True
    while menu:
        print('#########################')
        print('1 - Tentar fazer requisição')
        print('2 - Ver tempo restante do bloqueio')
        print('3 - Sair')
        print('#########################')
        opcao = input('Digite sua opção... ')
        match opcao:
            case '1':
                user_id = input('Digite o ID do usuário: ')
                if limiter.permitir_requisicao(user_id):
                    print("Requisição permitida!")
                    limpar_terminal_com_atraso()

                else:
                    print("Limite atingido! Requisição bloqueada.")
                    limpar_terminal_com_atraso()
            case '2':
                user_id = input('Digite o ID do usuário: ')
                ttl = limiter.tempo_restante(user_id)
                
                if ttl == -2:
                    print("Nenhuma requisição registrada para esse usuário.")
                    limpar_terminal_com_atraso()
                elif ttl == -1:
                    print("Chave sem tempo de expiração definido.")
                    limpar_terminal_com_atraso()
                else:
                    print(f"Tempo restante para resetar o limite: {ttl} segundos.")
                    limpar_terminal_com_atraso()
            case '3':
                print('Saindo...')
                limpar_terminal_com_atraso()
                menu = False
            case _:
                print('Opção inválida.')
                limpar_terminal_com_atraso()
