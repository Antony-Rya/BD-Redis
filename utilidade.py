import os
import time

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def limpar_terminal_com_atraso(segundos=3):
    print(f"\nA tela será limpa em {segundos} segundos...")
    time.sleep(segundos)
    os.system('cls' if os.name == 'nt' else 'clear')