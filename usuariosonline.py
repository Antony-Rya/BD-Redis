from utilidade import limpar_terminal_com_atraso

class UsuariosOnline:
    def __init__(self, r):
        self.redis = r
        self.key = "usuarios_online"

    def conectar_usuario(self, usuario_id):
        self.redis.sadd(self.key, usuario_id)
        print(f"Usuário '{usuario_id}' está online.")

    def desconectar_usuario(self, usuario_id):
        self.redis.srem(self.key, usuario_id)
        print(f"Usuário '{usuario_id}' saiu.")

    def listar_usuarios_online(self):
        usuarios = self.redis.smembers(self.key)
        if usuarios:
            print("Usuários online:")
            for usuario in usuarios:
                print(usuario)
        else:
            print("Nenhum usuário online no momento.")

def usuariosmenu(usuarios_online):
    menu = True
    while menu:
        print('#################')
        print('1 - Adicionar usuário online')
        print('2 - Remover usuário online')
        print('3 - Listar usuários online')
        print('4 - Sair')
        print('#################')
        opcao = input('Digite sua opção... ')
        match opcao:
            case '1':
                usuario_id = input('Digite o ID do usuário: ')
                usuarios_online.conectar_usuario(usuario_id)
                limpar_terminal_com_atraso()
            case '2':
                usuario_id = input('Digite o ID do usuário a remover: ')
                usuarios_online.desconectar_usuario(usuario_id)
                limpar_terminal_com_atraso()

            case '3':
                usuarios_online.listar_usuarios_online()
            case '4':
                print('Saindo...')
                limpar_terminal_com_atraso()

                menu = False
            case _:
                print("Opção inválida.")
                limpar_terminal_com_atraso()

