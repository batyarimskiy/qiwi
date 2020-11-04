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

      by @batyarimskiy  v.1
 """
print(intro)

token=input('Введите токен: ')
phone=input('Введите номер: ');

menu = """
1. Баланс
2. Перевести деньги
"""

def pay():
    api = QApi(token=token, phone=phone)
    print(api.balance)
    api.pay(account="ТЕЛЕФОН ПОЛУЧАТЕЛЯ", amount=1, comment='Привет мир!')
    print(api.balance)

def balans():
    api = QApi(token=token, phone=phone)
    print('Ваш баланс')
    print(api.balance)
    print('вы нириально багат!')                                                                
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
