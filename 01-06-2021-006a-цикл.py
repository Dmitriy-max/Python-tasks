# Получаем от пользователя число.
number = input('Enter range maximum value> ')
print()
# Находим длину числа.
numberLen = len(number)
# print(numberLen) выводим для отладки программы полученную длину.
# Если пользователь не ввел ни одного числа выходим из программы с кодом 1.
if numberLen == 0:
    print('Input number. Please, try again...')
    exit(1) 
# Если пользователь ввел буквенное значение выходим из программы с кодом 1.
if  type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Incorrect input. Please input one number, not word or numbers. Try again...")
        exit(1)
# Если пользователь ввел отрицательное число выходим из программы с кодом 1.
numberInt = int(number)
if numberInt < 0:
    print('Please, input positive number. Try again...')
    exit(1)
# Создаем цикл и выводим данные на экран.
for i in range(0,numberInt+1):
    print (i)
print()
print('Thanks for using our application')
print('(c) 2021 Dmitry Detukov')
print()