# получить предложение от пользователя
sentence = input('Enter your sentence> ')

# Времемнно выводим количество на экран (для отладки)
# print("'%s'" % sentence)

# Отступ пустой строки (после ввода пользователя)
print()

# Вычисляем длинну массива введенного предложения
sentenceLen = len(sentence)

if sentenceLen == 0:
    # Если пользователь не ввел слова, то выходим из программы с кодом один
    print("Bad user input. Please try again...")
    print()
    exit(1)

# разбить предложение на слова (в массив)
words = sentence.split()

# Вычисляем длинну массива введенных слов
totalWords = len(words)

# Времемнно выводим количество на экран (для отладки)
# print(totalWords)

# Инициализируем переменную в которой будет индекс самого длинного слова
# По умолчанию указывам на первое слово (индекс 0)
maxWordIndex = 0

if totalWords > 1:
    # Строим перебор по индексам массива начиная со второго слова (индекс 1)
    for wordIndex in range(1, totalWords):

        # Времемнно выводим индекс на экран (для отладки)
        # print(wordIndex)

        # Запоминаем текущее слово в локальную переменную
        word = words[wordIndex]

        # Времемнно выводим слово на экран (для отладки)
        # print(word)

        # получаем длинну текущего слова
        wordLen = len(word)

        # Времемнно выводим длинну слова для отладки
        # print(wordLen)

        # Определяем максималью длинну слова (известную на данный момент)
        maxWord = words[maxWordIndex]
        maxWordLen = len(maxWord)

        # сравниваем длинну текущего слова с максимальной ранее найденной длинной
        if wordLen > maxWordLen:

            # Если длинна текущего слова больше чем максимальная длинна
            # то запонимаем индекс этого слова
            maxWordIndex = wordIndex

        # Печатаем пустую строку (для отладки)
        # print()

# по окончанию цикла, у нас есть:
#  индекс максимально длинного слова если слова были введены
#  или -1 если слов не было

# Печатаем значение индекса (для отладки)
# print(maxWordIndex)

if maxWordIndex == -1:
    print("Bad user input. Please try again...")
else:
    # Запоминаем целевое (самое длинное) слово в локальную переменную
    targetWord = words[maxWordIndex]

    # Расчитывем человеко читаемую позицию в локальную переменную
    targetWordPos = maxWordIndex + 1

    # Вычисляем длинну нашего целевого слова в локальную переменную
    targetWordLen = len(targetWord)

    # Выводим на экран результаты
    print("Max word length: %s" % targetWordLen)
    print("Word position: %d" % targetWordPos)

print()
print("Thanks for using our application")
print("(c) 2021 Maksym Anurin")
print()
