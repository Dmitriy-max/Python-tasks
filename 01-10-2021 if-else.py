while True:
    money = input('Сколько у Вас денег?')
    a_money = int(money)
    if a_money < 0:
        print('Ты лузер!)))')
    elif a_money > 0:
        print('Красавчик!')
    if a_money == 0:
        break