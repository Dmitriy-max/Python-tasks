sentence = input('Enter your sentence> ')
words = sentence.split(sep=" ")
maxWordLen = 0
for word in words:
    wordLen = len(word)
    if wordLen > maxWordLen:
        maxWordLen = wordLen
print('\nMaximum word length is: %d'%maxWordLen)
maxIndex = 0
for index in range (len(words)):
    if (len(words[index]) > len(words[maxIndex])):
        maxIndex = index
print('Word position: ',maxIndex + 1)
print('\n\nThanks for using our application\n(c) 2021 Dmitry Detukov')

#Enter your sentence> Genius is one percent inspiration and ninety-nine percent perspiration

#Maximum word length: 12
#Word position: 9


#Thanks for using our application
#(c) YEAR Name Surname

    

        

   
 
     
    
    
    
    

    
        
    







