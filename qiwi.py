import os
import sys
import random

from modules import misc
from modules.qiwi_wrapper import QiwiWrapper
from modules.db_wrapper import DataBaseWrapper

db = DataBaseWrapper("accounts.db")
accounts = db.get_accounts()

misc.print_banner( len(accounts) )

proxy = input("Использовать прокси? (Y/n) ")
print()

if proxy == "y":
    if os.path.exists("proxy.txt"):
        with open("proxy.txt", "r") as f:
            proxies = f.read()

            if not proxies:
                print("Заполните файл proxies.txt")
                sys.exit()
            else:
                proxies = proxies.split("\n")

    else:
        with open("proxy.txt", "x"):
            pass

        print("Заполните файл proxy.txt IP адресами прокси-серверов")
        print("Например:")
        print()
        print("http://1.3.45.66.22:8080")
        print("http://154.46.114:80")

        sys.exit()

else:
    proxies = ["localhost"]

misc.print_banner( len(accounts) )

if not accounts:
    token = input("Введите токен от QIWI: ")
    number = input("Введите логин от QIWI: ")

    db.add_account(number, token)
    misc.print_banner( len(accounts) )

else:
    if len(accounts) == 1:
        qiwi = QiwiWrapper( accounts[0][1], accounts[0][0], proxy={"http": random.choice(proxies)} )
    else:
        for index, account in enumerate(accounts):
            print(f"{index + 1}. {account[0]}")

        print()

        while True:
            acc = input("Выберите аккаунт: ")

            if acc.isdigit():
                acc = int(acc)
                acc -= 1

                qiwi = QiwiWrapper(accounts[acc][1], account[acc][0], proxy={"http": random.choice(proxies)})
                misc.print_banner( len(accounts) )
                break
            else:
                print(f"{acc} - разве это похоже на число?")

while True:
    ch = misc.menu( len(accounts) )

    if ch.isdigit():
        ch = int(ch)

        if ch == 1:
            print(f"Баланс этого аккаунта: {qiwi.api.balance[0]}₽")

        if ch == 2:
            print(f"Баланс: {qiwi.api.balance[0]}₽")

            number = input('Номер кошелька: ')
            money = input('Сумма перевода: ')
            comment = input('Коментарий к переводу (нажмите ENTER, чтобы пропустить): ')

            qiwi.api.pay(account=number, amount=money, comment=comment)
            print('Перевод выполнен!')

        if ch == 3:
            token = input("Введите токен от QIWI: ")
            number = input("Введите логин от QIWI: ")

            db.add_account(number, token)

            misc.print_banner( len(accounts) )
            print("Аккаунт добавлен")

        if ch == 4:
            number = input("Введите логин от QIWI: ")
            db.delete_account(number)

            misc.print_banner( len(accounts) )
            print("Аккаунт удалён")

        if ch == 5:
            print(misc.authors)

        print()
    else:
        misc.print_banner( len(accounts) )