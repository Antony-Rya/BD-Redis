import redis

class Tarefa:
    def __init__(self, r):
        self.redis = r
        self.key = 'tarefas'

    def adicionar(self, descricao):
        self.redis.rpush('tarefas', descricao)

    def remover(self, index):
        lista = self.listar()
        if index > 0 and index < len(lista):
            tarefa = lista[index]
            self.redis.lrem('tarefas', 1, tarefa)

    def listar(self):
        return self.redis.lrange('tarefas', 0, -1)
    

