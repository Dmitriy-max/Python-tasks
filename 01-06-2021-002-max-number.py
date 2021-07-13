# получаем от пользователя три числа
num1 = input('Enter first number> ')
num2 = input('Enter second number> ')
num3 = input('Enter third number> ')
print()
# Если пользователь не ввел ни одного числа выходим из программы с кодом 1.
if num1 == "" or num2 == "" or num3 == "":
  print()
  print('Incorrect input. Please try again...')
  exit(1)
# Если пользователь ввел буквенное значение выходим из программы с кодом 1.
if  num1.isalpha() or num2.isalpha() or num3.isalpha():
        print("Incorrect input. Please input numbers, not words. Try again...")
        exit(1)
# Полученные от пользователя данные из строки переводим в числовое значение.
number1 = int(num1)
number2 = int(num2)
number3 = int(num3)
# выводим на экран переменные в которых хранятся полученные данные. 
print('Your values are stored in variables:')
print('     a =',number1)
print('     b =',number2)
print('     c =',number3)
print('Checking maximum value... Please wait...')
# Инициализируем переменную в которой будем хранить полученные значения.
numberMas = [number1,number2,number3]
print('Maximum value is:')


#Находим максимальное значение введенных чисел и выводим их на экран.
if number2 < number1 > number3:
        print('   ',number1)
elif number1 < number2 > number3:
        print('   ',number2)
else:
        print('   ',number3)

print('Thanks for using our application')
print('(C) 2021 Dmitry Detukov')





# Выводим на экран результаты 

#Ожидаемый результат работа программы:

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
#(c) YEAR Name Surname

