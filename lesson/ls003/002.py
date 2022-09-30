# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import choices

def getRandomList(size,chars):
    words=[]
    for i in range(size):
        word=choices(chars, k=3)# new word
        words.append("".join(word))# word into words
    return words

def findIndex(word,words):
    if word in words and words.count(word)>1:
        firstIndex=words.index(word)
        print(words.index(word, firstIndex+1))
    else:
        print(-1)

words=getRandomList(10,"xyz")
print(words)
findIndex(input(), words)
