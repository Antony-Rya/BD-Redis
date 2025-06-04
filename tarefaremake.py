import redis

class Tarefa:
    def __init__(self, r):
        self.redis = r
        self.key = 'tarefas'

    def adicionar(self, descricao):
        self.redis.rpush('tarefas', descricao)
