import random
num = random.randint(1,10)
while True:
    print('Введите число от 1 до 10:')
    num1 = int(input())
    if num1 == num:
        print('Вы угадали число! Поздравляю, Вы умка!!!')
        break
    else :
        print('Вы не угадали число! Вы лузер')
    if num1 == 1000:
        print('Загаданное число: %s' %num)


  