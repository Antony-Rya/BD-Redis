"""Basic connection example.
"""

import redis
from tarefaremake import Tarefa, tarefamenu
from ranking import Ranking, rankingmenu
from contador import ContadorAcessos, contadormenu
from usuariosonline import UsuariosOnline, usuariosmenu
from ratelimiter import RateLimiter, ratelimitermenu

r = redis.Redis(
    host='redis-19001.c336.samerica-east1-1.gce.redns.redis-cloud.com',
    port=19001,
    decode_responses=True,
    username="default",
    password="CkZcXjVN8EpjIWmJEt0IrhoT2xNWSGCP",
    
)


contador = ContadorAcessos(r)
ranking = Ranking(r)
tarefas = Tarefa(r)
usuarios = UsuariosOnline(r)
ratelimiter = RateLimiter(r)



def menuprincipal():
    menu = True
    while menu:
        print('#########################')
        print('1 - tarefas')
        print('2 - contador')
        print('3 - usuarios online')
        print('4 - limitador de acesso')
        print('5 - ranking')
        print('#########################')
        opcao = input('Digite sua opção... ')
        match opcao:
            case '1':
                tarefamenu(tarefas)
            case '2':
                contadormenu(contador)
            case '3':
                usuariosmenu(usuarios)
            case '4':
                ratelimitermenu(ratelimiter)
            case '5':
                rankingmenu(ranking)
            case _:
                print('Opção inválida.')
                limpar_terminal_com_atraso()

menuprincipal()
