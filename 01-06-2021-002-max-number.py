# получаем от пользователя три числа
num1 = input('Enter first number> ')
num2 = input('Enter second number> ')
num3 = input('Enter third number> ')
if num1 == "" or num2 == "" or num3 == "":
  print()
  print('Incorrect input. Please try again...')
  exit(1)
  # полученные от пользователя данные из строки переводим в числовое значение
num4 = int(num1)
num5 = int(num2)
num6 = int(num3)
# выводим на экран переменные в которых хранятся полученные данные 
print('Your values are stored in variables:')
print('     a =',num4,'  \n     b =',num5,'  \n     c =',num6)
print('Checking maximum value... Please wait...')
maxNum = [num4,num5,num6] # инициализируем переменную в которой будем хранить полученные значения
print('Maximum value is:')
print("  ",max(maxNum)) # выводим на экран результаты 
#(при помощи функции max находим максималььное значение введенных чисел)

print('Thanks for using our application')
print('(C) 2021 Dmitry Detukov')

#Ожидаемый результат работы программы:

#Enter first number> 12
#Enter second number> -200
#Enter third number> 67
#Your values are stored in variables:
#a = 12
#b = -200
#c = 67
#Checking maximum value... Please wait...
#Maximum value is:
 #  67
#Thanks for using our application
