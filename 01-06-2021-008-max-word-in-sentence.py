
sentence = input("Enter your sentence> ")
words = sentence.split()
maxWordLen = 0
#print(words)
for word in words:
    wordLen = len(word)
    if wordLen > maxWordLen:
        maxWordLen = wordLen
#print(wordLen)
    
print('\nMaximum word length:',maxWordLen)
print('\n\nThanks for using our application\n(c) 2021 Dmitry Detukov')

#Ожидаемый результат работы программы:

#Enter your sentence> Genius is one percent inspiration and ninety-nine percent perspiration

#Maximum word length: 12


#Thanks for using our application
#(c) YEAR Name Surname


