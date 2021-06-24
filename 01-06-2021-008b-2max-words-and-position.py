# Получаем предложение от пользователя
sentence = input('Input your sentence> ')
print()
# Разбиваем полученное предложение на массив слов.
words = sentence.split()
# Вычисляем длину массива.
wordsLen = len(words)
# Выводим длину массива для отладки программы.
if wordsLen == 0:
    # Если пользователь не ввел слова, то выходим из программы с кодом один.
    print("Bad user input. Please try again...")
    print()
    exit(1)
if wordsLen == 1:
    # Если пользователь ввел одно слово, то выходим из программы с кодом один.
    print("Bad user input. Please input few words.")
    print()
    exit(1)
# Инициализируем переменную в которой будет длина самого длинного слова, по умолчанию 0.
maxWordLen = 0
# Инициализируем переменную в которой индекс самого длинного слова
# По умолчанию указывам на первое слово (индекс 0).
maxWordIndex = 0
# Через цикл строим перебор по словам массива.
for word in range(wordsLen):
    # Запоминаем текущее слово в локальную переменную.
    currentWord = words[word]
    currentWordLen = len(currentWord)
    #  Определяем максималью длинну слова (известную на данный момент)
    if currentWordLen > maxWordLen:
        # Если длинна текущего слова больше чем максимальная длинна, которая была по умолчанию
        # то запонимаем это слово.
        maxWordLen = currentWordLen 
        # Если длинна текущего слова больше чем максимальная длинна,
        # то запонимаем индекс этого слова и для человекочитабельности добавляем 1.
        maxWordIndex = word + 1
# Ищем макс. длинное второе слово по аналогии с первым.
maxWordLen2 = 0 
maxWordIndex2 = 0 
for word2 in range (wordsLen): 
    currentWord2 = words[word2]
    currentWordLen2 = len(currentWord2)
    #print(currentWordLen2) 
    # Если длинна текущего слова меньше чем найденая ранее максимальная длинна и больше
    # макс. длины, которая была по умолчанию то запонимаем это слово в переменную.
    if  currentWordLen2 < maxWordLen and currentWordLen2 > maxWordLen2:
        maxWordLen2 = currentWordLen2
        maxWordIndex2 =  word2 + 1
# Выводим результаты на экран.
print("Maximum word length1: %s"%maxWordLen) 
print('Word position1: %s' % maxWordIndex)
print()
print()
print("Maximum word length2: %s"%maxWordLen2)
print('Word position2: %s' % maxWordIndex2)
print()
print("Thanks for using our application")
print("(c) 2021 Dmitry Detukov")
print()



