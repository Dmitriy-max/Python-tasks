sentence = input('Input your sentence> ')
words = sentence.split()
wordsLen = len(words)
maxWordLen = 0
maxWordIndex = 0
for word in range(wordsLen):
    
    if len(words[word]) > maxWordLen:
        maxWordLen = len(words[word])
        maxWordIndex = word+1

    
print("Длинное слово: %s"%maxWordLen)
print('Index %s' % maxWordIndex)