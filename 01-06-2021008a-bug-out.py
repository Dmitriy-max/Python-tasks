# Получаем предложение от пользователя.
sentence = input('Input your sentence> ')
# Разбиваем предложение на массив слов.
words = sentence.split()
# Находим длину массива.
wordsLen = len(words)
print()
if wordsLen == 0:
    # Если пользователь не ввел слова, то выходим из программы с кодом один.
    print("Bad user input. Please try again...")
    print()
    exit(1)
maxWordIndex = 0
maxWordLen = 0
maxWordIndex2 = 0
maxWordOne = 0
# Находим макс. длинное первое слово и его индекс, по умолчанию текущее длинное слово приравниваем к 0.
# Делаем перебор слов через (через цикл).
for wordindex in range(wordsLen):
# находим макс. длинное первое слово.
    maxWord = words[wordindex]
    WordLen = len(maxWord)
# Сравниваем длину текущего слова и перовначального.
    if WordLen > maxWordLen:
# Если текущее слово длиннее в локальную переменную записываем полученное значение.
       maxWordLen = WordLen 
# В переменную записываем индекс макс. слова и для человекочитабельности добавляем единицу. 
       maxWordIndex = wordindex + 1
# Находим максимально длинное второе слово и его индекс по аналогии с первым.
    maxWord2 = words[wordindex]
    WordLen2 = len(maxWord2)
    if WordLen2 == maxWordLen:
        maxWordLen2 = WordLen2
        maxWordIndex2 = wordindex + 1
# Если пользователь ввел одно макс. слово в предложении, выходим из программы с кодом 1.
if maxWordLen == maxWordLen2 and maxWordIndex == maxWordIndex2:
# Выводим данные на экран.
    print('Maximum word one: ',maxWordLen)
    print('Maximum word one index: ',maxWordIndex)
    exit(1)
# Выводим данные на экран если макс. слов два.
print('Maximum word1 length: ',maxWordLen)
print('Maximum wird1 index: ',maxWordIndex)
print()
print('Maximum word2 length: ',maxWordLen2)    
print('Maximum wird2 index: ',maxWordIndex2)
print()
print()
print('Thanks for using our application')
print('(c) 2021 Dmitry Detukov')






    
  


    