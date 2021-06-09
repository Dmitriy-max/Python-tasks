# получаем предложение от пользователя 
sentence = input("Enter your sentence> ")
words = sentence.split() # разбиваем предложение на массив слов
# print(words) временно выводим массив для отладки программы
maxWordLen = 0 # инициализируем переменную, в которой будет max значение слова(изначально самое длинное слово==0)
for word in words: # строим перебор по словам массива 
    wordLen = len(word) 
    # print(wordLen) # временно выводим переменную для отладки программы
    if wordLen > maxWordLen:#  сравниваем длинну текущего слова с максимальной ранее найденной длинной
        maxWordLen = wordLen # если длина текущего слова больше ранего, запоминаем его в переменную
print()# выводим результаты на экран
print('Maximum word length:',maxWordLen)
print()
print()
print('Thanks for using our application')
print()
print('(c) 2021 Dmitry Detukov')

#Ожидаемый результат работы программы:

#Enter your sentence> Genius is one percent inspiration and ninety-nine percent perspiration

#Maximum word length: 12


#Thanks for using our application
#(c) YEAR Name Surname


