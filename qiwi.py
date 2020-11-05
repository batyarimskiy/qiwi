import os
from SimpleQIWI import *

clear = ('clear')

os.system(clear)

intro = """
  ___  _          _
 / _ \(_)_      _(_)
| | | | \ \ /\ / / |
| |_| | |\ V  V /| |
 \__\_\_| \_/\_/ |_|

      by @batyarimskiy  v.1.1
 """
print(intro)

token=input('Введите токен: ')
phone=input('Введите номер: ');

menu = """
1. Баланс
2. Перевести деньги
"""

def balans():
    api = QApi(token=token, phone=phone)
    print('Ваш баланс')
    print(api.balance)
    print('вы нириально багат!')
    print("""

Чтобы выйти в главное меню нажмите Enter:
    """)
    input()

def pay():
    api = QApi(token=token, phone=phone)
    print('ваш баланс')
    print(api.balance)
    pay=input('Номер получателя: ')
    sym=input('Сумма перевода: ')
    com=input('Коментарий к переводу: ')
    api.pay(account=pay, amount=sym, comment=com)
    print(api.balance)
    print("""

Чтобы выйти в главное меню нажмите Enter:
    """)
    input()

def main():
    os.system(clear)
    print(intro)
    print(menu)
    num_menu = input("[+] > ")
    if num_menu == "1":
        balans()
    if num_menu == "2":
        pay()
    else:
        main()
main()
