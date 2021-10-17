number = int(input('Input your number> '))
for j in range(number+1):
    for i in range(j):
        print(j, end=" ") # вывод числа
    # вывод пустой строки после каждой строки с числами для правильного отображения шаблона
    print(" ")