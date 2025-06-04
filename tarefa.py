# import uuid
# import json

# class Tarefa:
#     def __init__(self, redis_conn):
#         self.redis = redis_conn
#         self.key = "tarefas"

#     def adicionar_tarefa(self, descricao):
#         id_tarefa = str(uuid.uuid4())
#         tarefa = {'id': id_tarefa,'descricao': descricao, 'concluida': False}
#         self.redis.rpush(self.key, json.dumps(tarefa))
#         return id_tarefa
        
#     def listar(self):
#         tarefas_serializadas = self.redis.lrange(self.key, 0, -1)
#         return [json.loads(tarefa) for tarefa in tarefas_serializadas]
    
#     def remover(self, tarefa_id):
#         tarefas = self.listar()
#         for tarefa in tarefas:
#             if tarefa["id"] == tarefa_id:
#                 self.redis.lrem(self.key, 1, json.dumps(tarefa))
#                 return True
#         return False