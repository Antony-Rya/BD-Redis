from utilidade import limpar_terminal
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


menu = True
def tarefamenu(tarefas):

    global menu
    while menu:
        limpar_terminal()
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

