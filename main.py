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
ratelimitermenu(ratelimiter)