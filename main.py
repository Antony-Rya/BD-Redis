"""Basic connection example.
"""

import redis
from tarefaremake import Tarefa, tarefamenu

r = redis.Redis(
    host='redis-19001.c336.samerica-east1-1.gce.redns.redis-cloud.com',
    port=19001,
    decode_responses=True,
    username="default",
    password="CkZcXjVN8EpjIWmJEt0IrhoT2xNWSGCP",
    
)




tarefas = Tarefa(r)
tarefamenu(tarefas)