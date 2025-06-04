"""Basic connection example.
"""

import redis
from tarefa import Tarefa

r = redis.Redis(
    host='redis-19001.c336.samerica-east1-1.gce.redns.redis-cloud.com',
    port=19001,
    decode_responses=True,
    username="default",
    password="CkZcXjVN8EpjIWmJEt0IrhoT2xNWSGCP",
    
)

menu = True
while menu:
    print('#################')
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Remover tarefas')
    print('4 - Sair')
    print('#################')
    opcao = input('Digite sua opção... ')
    match opcao:
        case '1':
            print('Digite a descrição da sua tarefa: ')
            descricao = input()
            tarefa = Tarefa(descricao)
            print(tarefa)
        case '2':
            print('listar tarefas')
        case '3':
            print('remover tarefa')
        case '4':
            print('saindo...')
            menu = False