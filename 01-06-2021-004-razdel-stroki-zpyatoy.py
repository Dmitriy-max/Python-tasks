# Получаем данные от пользователя
sentence = input('Enter your name and surname> ')
print()
# Разбиваем предложение на массив по запятую.
words = sentence.split(',')
# print(words)
sentenceLen = len(sentence)
# print(wordsLen)
if sentenceLen == 0:
    print('Please, Enter your name and surname. Try again...')
    exit(1) 
for i in range (sentenceLen):
        if sentence[i].isdigit():
                print('Please, Enter your name and surname. Try again...')
                exit(2) 

print(words[0]) # выводим первое слово
print(words[1]) # выводим второе слово
print()
print()
print('Thanks for using our application')
print('(c) 2021 Dmitry Detukov')

# Ожмдаемое:
#Enter your name and surname> Ivan,Sidorov

#Ivan
#Sidorov


#Thanks for using our application
#(c) YEAR Name Surname



