"""Basic connection example.
"""

import redis
from tarefaremake import Tarefa

r = redis.Redis(
    host='redis-19001.c336.samerica-east1-1.gce.redns.redis-cloud.com',
    port=19001,
    decode_responses=True,
    username="default",
    password="CkZcXjVN8EpjIWmJEt0IrhoT2xNWSGCP",
    
)

menu = True
tarefas = Tarefa(r)
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
            tarefas.adicionar(descricao)
            print('Tarefa adicionada com sucesso"')
        case '2':
            lista = tarefas.listar()
            print("Tarefas:")
            for i, item in enumerate(lista):
                print(f"{i} - {item}")

        case '3':
            print('Digite o indice da tarefa que deseja remover: ')
            index = int(input())
            tarefas.remover(index)
        case '4':
            print('saindo...')
            menu = False