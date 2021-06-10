


#получаем предложение от пользователя
sentence = input('Enter any sentence with comma: ')

# вычисляем длину введенного предложения
sentenceLen = len(sentence)

#выводим длину введенного предложения для отладки программы
# print(sentenceLen)

# если пользователь ничего не ввел выходим из программы с кодом 1
if sentenceLen == 0:
    print()
    print('Comma is not found. Incorrect input sentence. Please try again...')
    exit(1)

commaPosition = sentence.find(',')

# если пользователь ввел предложение без запятой, выходим из программы с кодом 1
if commaPosition == -1:
    print()
    print('Comma is not found. Incorrect input sentence. Please try again...')
    exit(1)

# для человекочитаемости к индексу запятой добавляем 1
humanFriendlyPos = commaPosition + 1

# выводим результат на экран
print()
print('Comma is found at position:', humanFriendlyPos)
print()
print()
print('Thanks for using our application')
print('(C) 2021 Dmitry Detukov')

#Ожидаемый результат работы программы:

#Enter any sentence with comma> Ivan,Sidorov

#Comma is found at position: 5


#Thanks for using our application


