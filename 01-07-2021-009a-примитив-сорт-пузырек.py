# Получаем от пользователя ряд чисел.
numbers = input('Input some numbers> ')
print()
# Разбиваем на массив ряд чисел.
numbersMas = numbers.split()
# print(numbersMas) выводим полученный массив для отладки программы.
# Вычисляем длинну массива введенных чисел.
numbersLen = len(numbersMas)
# print(numsLen) выводим длинну массива для отладки программы.
# Если пользователь не ввел ни одного числа, то выходим из программы с кодом 1.
if numbersLen == 0:
    print('Input numbers. Please, try again...')
    exit(1) 

# Проводим проверку если пользователь ввел буквенное значение выходим из программы с кодом 2.

for j in range(numbersLen):
    if  type(numbersMas[j]) != int:
        try:
            numbersMas[j] = int(numbersMas[j])
        except ValueError:
            print("Incorrect input. Please input only numbers, not words. Try again...")
            exit(2)
        # Переводим значения str массива в значения int и создаем навый массив с числами-normalizedNumbersMas.
        valueStr = numbersMas[j]
        valueInt = int(valueStr)
        numbersMas[j] = valueInt
        normalizedNumbersMas = numbersMas
        # Выводим для отладки массив с числами.
        #print(normalizedNumbersMas)
# Сортируем массив в порядке убывания.
for i in range(numbersLen):    
    # Создаем вложенный цикл для перебора чисел и нахождения меньшего по значению числа.
    # Меньшее число ставим перед большим.
        for n in range(0,numbersLen-i-1):
                if normalizedNumbersMas[n] < normalizedNumbersMas[n+1]:
                    # Вводим локальную переменную-localnumber для обмена переменных.
                        localnumber = normalizedNumbersMas[n+1]
                        normalizedNumbersMas[n+1] = normalizedNumbersMas[n]
                        normalizedNumbersMas[n] = localnumber
print('Your numbers in descending orders:')
# Выводим элементы массива на экран.
for i in range(numbersLen): 
        print(normalizedNumbersMas[i])
print()
print('Thanks for using our application')
print('(c) 2021 Dmitry Detukov')
print()




