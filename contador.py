from utilidade import limpar_terminal, limpar_terminal_com_atraso

class ContadorAcessos:
    def __init__(self, r):
        self.redis = r

    def registrar_acesso(self, item: str):
        self.redis.incr(item)
        print(f"Acesso registrado para '{item}'")

    def obter_acessos(self, item: str):
        acessos = self.redis.get(item)
        return int(acessos) if acessos else 0


menu = True

def contadormenu(contador):
    global menu
    while menu:
        # limpar_terminal()
        print('#################')
        print('1 - Registrar acesso')
        print('2 - Consultar acessos de um item')
        print('3 - Sair')
        print('#################')
        opcao = input('Digite sua opção... ')
        match opcao:
            case '1':
                item = input('Digite o nome do item: ')
                contador.registrar_acesso(item)
                limpar_terminal_com_atraso()
            case '2':
                item = input('Digite o nome do item para consultar: ')
                acessos = contador.obter_acessos(item)
                print(f"O item '{item}' foi acessado {acessos} vezes.")
                limpar_terminal_com_atraso()

            case '3':
                print('Saindo...')
                limpar_terminal_com_atraso()

                menu = False
            case _:
                print("Opção inválida.")
                limpar_terminal_com_atraso()


