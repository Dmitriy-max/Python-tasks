# получаем от пользователя два числа
num1 = input('Enter first number> ')
num2 = input ('Enter second number> ')
# Если пользователь не ввел слова, то выходим из программы с кодом один
if num1 == ("") or num2 == (""):
  print()
  print('Incorrect input. Please try again...')
  exit(1)
  # полученные от пользователя данные из строки переводим в числовое значение
num3 = int(num1)
num4 = int(num2)
# выводим на экран переменные где хранятся введенные значения
print ('Your values are stored in variables:' )
print('   a =',num3)
print('   b =',num4)
print('Switching values... Please wait...')
numChange = num3 # инициализируем переменную при помощи, которой будет происходить обмен введенных чисел
num3 = num4
num4 = numChange
print('Values after switching:') 
print ('   a =',num3) # выводим данные после обмена
print ('   b =',num4) 
Sum = num3 + num4 # вводим переменную в которой будет храниться сумма чисел после обмена 
print('Summa:')
print ('  c =',Sum) # выводим сумму чисел на экран
print('Thanks for using our application')
print('(C) 2021 Dmitry Detukov')

#Ожидаемый результат работы программы:

#Enter first number> 12
#Enter second number> 45
#Your values are stored in variables:
 #  a = 12
  # b = 45
#Switching values... Please wait...
#Values after switching:
 #  a = 45
  # b = 12
#Summa:
 #  с = 57
#Thanks for using our application


