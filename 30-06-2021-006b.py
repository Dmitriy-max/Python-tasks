#Получаем от пользователя два числа.
number1 = input('Enter range maximum value> ')
number2 = input('Enter multiple value> ')
print()
print()
# Находим длину чисел.
numberLen1 = len(number1)
numberLen2 = len(number2)
# Выводим для отладки программы полученные длины.
# print(numberLen1, numberLen2)
# Если пользователь не ввел ни одного числа выходим из программы с кодом 1.
if numberLen1 == 0 or numberLen2 == 0:
    print('Input numbers. Please, try again...')
    exit(1) 
# Если пользователь ввел буквенное значение выходим из программы с кодом 1.
if  type(number1) != int or type(number2) != int:
    try:
        number1 = int(number1)

    except ValueError:
        print("Incorrect input. Please input numbers, not words. Try again...")
        exit(1)
# Если пользователь ввел отрицательные числа выходим из программы с кодом 1.
numberInt1 = int(number1)
numberInt2 = int(number2)
if numberInt1 < 0 or numberInt2 < 0:
    print('Please, input positive number. Try again...')
    exit(1)
# Создаем цикл для перебдра значений, указываем шаг и выводим данные на экран.
for n in range (0,numberInt1+1,numberInt2):
    print(n)
print()
print('Thanks for using our application')
print('(c) 2021 Dmitry Detukov')
print()