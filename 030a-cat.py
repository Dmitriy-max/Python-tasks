#!/usr/bin/python 
# Для того чтобы не запускать программу каждый раз через python, пишем верхнюю строку:#!/usr/bin/python.
# Импортируем модуль sys.
import sys
# Вводим переменную в которую вкладываем (в виде массива) аргументы командной строки.
masFile = sys.argv
# print(masFile) - для отладки программы выводим на экран массив.
# Находим длину массива.
masFileLen = len(masFile)
# print(masFileLen) - для отладки программы выводим на экран длину массива.
# Перебираем массив 
for i in range (masFileLen):
# В локальную переменную вкладываем занчение последнего аргумента командной строки (название файла).
    lastFile = masFile[i]
# Отркрываем файл, читаем его и выводим в консоль.
with open(lastFile,'rt') as file:
    text = file.read()
    print(text)



print('Thanks for using our utility tools.')
print('(c) 2021 Dmitry Detukov')