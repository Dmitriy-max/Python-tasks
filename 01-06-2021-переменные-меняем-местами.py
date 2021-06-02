A = int(input('Enter first number> '))
B = int(input ('Enter second number> '))

print ('Your values are stored in variables:' )
print('   a =',A, '\n   b =',B)
print('Switching values... Please wait...')
D = A
A = B
B = D
print('Values after switching:')
print ('   a =',A,'\n   b =',B)
C = A + B
print('Summa:\n   c =',C)
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


