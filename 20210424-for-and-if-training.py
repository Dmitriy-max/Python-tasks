Задача 2
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона, к которому относится этот месяц.
Например, передаем 2, на выходе получаем 'Зима'.
def month_to_seas(n):
    if n == 1 or n == 2 or n == 12:
       return 'Зима'
    elif n == 3 or n == 4 or n == 5:
        return 'Весна'
    elif n == 6 or n == 7 or n == 8:
        return 'Лето'
    elif n == 9 or n == 10 or n == 11:
        return 'Осень'
    else: 
        return 'Укажите число от 1 до 12' 
if __name__=='__main__':
    print(month_to_seas(34))








     




      

