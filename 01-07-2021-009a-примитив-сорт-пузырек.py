# Получаем от пользователя ряд чисел.
numbers = input('Input some numbers: ')
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

# Проводим проверку если пользователь ввел буквенное значение выходим из программы с кодом 1.
for j in range(numbersLen):
 if  type(numbersMas[j]) != int:
    try:
        numbersMas[j] = int(numbersMas[j])
    except ValueError:
        print("Incorrect input. Please input only numbers, not words. Try again...")
        exit(1)

# Переводим значения str массива в значения int.
for i in range (numbersLen):
        valueStr = numbersMas[i]
        valueInt = int(valueStr)
        numbersMas[i] = valueInt
        
# Сортируем массив в порядке убывания.
for i in range(numbersLen):    
    # Создаем вложенный цикл для перебора чисел и нахождения меньшего по значению числа.
    # Меньшее число ставим перед большим.
        for n in range(0,numbersLen-i-1):
                if numbersMas[n] < numbersMas[n+1]:
                    # Вводим локальную переменную-localnumber для обмена переменных.
                        localnumber = numbersMas[n+1]
                        numbersMas[n+1] = numbersMas[n]
                        numbersMas[n] = localnumber
print('Your numbers in descending orders:')
# Выводим элементы массива на экран.
for i in range(numbersLen): 
        print(numbersMas[i])
print()
print('Thanks for using our application')
print('(c) 2021 Dmitry Detukov')
print()




