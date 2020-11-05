import os
from termcolor import colored

authors = colored("""Авторы данного скрипта:
@json1c (github: sergeyfilippov1, telegram: @json1c)
@batyarimskiy (github: batyarimskiy, telegram: @batyarimskiy)""", "cyan")

banner = colored("""
░██████╗░██╗░██╗░░░░░░░██╗██╗
██╔═══██╗██║░██║░░██╗░░██║██║
██║██╗██║██║░╚██╗████╗██╔╝██║
╚██████╔╝██║░░████╔═████║░██║
░╚═██╔═╝░██║░░╚██╔╝░╚██╔╝░██║
░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝""", "yellow")

def print_banner(count):
    os.system("clear")
    
    print(banner)
        
    print()
    print(f"Количество аккаунтов: {count}")
    print()

def menu(count):
    print("1. Узнать баланс")
    print("2. Перевод денег")
    print("3. Добавить ещё один аккаунт")
    print("4. Удалить аккаунт")
    print()
    print("5. Авторы")
    
    ch = input(">> ")
    print_banner(count)
    
    return ch