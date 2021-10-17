num = input("Enter your number> ")
nums = input('Enter '+ num +' numbers> ')
#print(nums)
numsMas = nums.split()
print(numsMas)
numsMasLen = len(numsMas)
#print(numsMasLen)
for i in range(numsMasLen):
    valueStr = numsMas[i]
    valueInt = int(valueStr)
    numsMas[i] = valueInt
    numsMasInt = numsMas
#print(numsMasInt)
z = 0
for j in numsMasInt:
    if j == 0:
      z += 1
print(z)


Дано N чисел: сначала вводится число N, 
затем вводится ровно N целых чисел. 
Подсчитайте количество нулей среди введенных чисел 
и выведите это количество. 
Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.

