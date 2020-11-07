import os
import sys
import random
import time

from termcolor import colored
from SimpleQIWI.Errors import QIWIAPIError
from progress.bar import IncrementalBar

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
    proxies = ["http://localhost"]

misc.print_banner( len(accounts) )

if not accounts:
    token = input("Введите токен от QIWI: ")
    number = input("Введите логин от QIWI: ")

    qiwi_ = QiwiWrapper(token, number, proxy={"http": random.choice(proxies)})

    try:
        _ = qiwi_.api.balance
        db.add_account(number, token)

        accounts = db.get_accounts()
        misc.print_banner( len(accounts) )
        print("Аккаунт добавлен")

    except:
        print()
        print("Токен невалидный")
        sys.exit()

if len(accounts) == 1:
    qiwi = QiwiWrapper( accounts[0][1], accounts[0][0], proxy={"http": random.choice(proxies)} )

elif len(accounts) > 1:
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
    try:
        ch = misc.menu( len(accounts) )
    
        if ch.isdigit():
            ch = int(ch)

            if ch == 1:
                token = input("Введите токен от QIWI: ")
                number = input("Введите логин от QIWI: ")

                qiwi_ = QiwiWrapper(token, number, {"http": random.choice(proxies)})

                try:
                    _ = qiwi_.api.balance
                    db.add_account(number, token)

                    accounts = db.get_accounts()
                    misc.print_banner( len(accounts) )
                    print("Аккаунт добавлен")
                except:
                    print()
                    print("Токен невалидный")
    
            if ch == 2:
                number = input("Введите логин от QIWI: ")
                db.delete_account(number)

                accounts = db.get_accounts()
                misc.print_banner( len(accounts) )
                print("Аккаунт удалён")

            if ch == 3:
                print(misc.authors)

            if ch == 4:
                print(f"Баланс этого аккаунта: {qiwi.api.balance[0]}₽")

            if ch == 5:
                print(f"Баланс: {qiwi.api.balance[0]}₽")
                print()

                number = input('Номер кошелька: ')
                money = input('Сумма перевода: ')

                while not money.isdigit():
                    print("Ты будешь переводить буквы?")
                    money = input('Сумма перевода: ')

                comment = input('Коментарий к переводу (нажмите ENTER, чтобы пропустить): ')

                if float(money) <= qiwi.api.balance[0]:
                    qiwi.api.pay(
                        account=number,
                        amount=money,
                        comment=comment
                    )
                    print('Перевод выполнен')
                else:
                    print()
                    print("Недостаточно средств")
                    input("Нажмите ENTER, чтобы продолжить")
                    misc.print_banner(len(accounts))

            if ch == 6:
                print(f"Ваш баланс: {qiwi.api.balance[0]}₽")
                print()
                print(misc.ban_account_desc)

                number = input('Номер кошелька: ')
                pays = input('Количество переводов (будет переведен один рубль): ')

                while not pays.isdigit():
                    print("Количество нужно указывать в цифрах")
                    pays = input('Количество переводов (переводы будут по рублю): ')

                comment = input('Коментарий к переводу (нажмите ENTER, чтобы пропустить): ')
                print()

                if float(pays) > qiwi.api.balance[0]:
                    print()
                    print("Недостаточно средств")
                    input("Нажмите ENTER, чтобы продолжить")
                    misc.print_banner(len(accounts))

                else:
                    bar = IncrementalBar( colored("Отправка платежей", "cyan"), max=int(pays))

                    for _ in range( int(pays) ):
                        qiwi.api.pay(
                            account=number,
                            amount=1,
                            comment=comment
                        )

                        time.sleep( 0.34 )
                        bar.next()

            print()
        else:
            misc.print_banner( len(accounts) )

    except KeyboardInterrupt:
        break
