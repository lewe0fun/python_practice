# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect
from random import sample

def getRandStr(size,chars):
    if size<1:
        return "The data is incorrect"
    words=[]
    for i in range(size):
        words.append("".join(sample(chars, len(chars))))
    return ' '.join(words)

def removeWords(words,word):
    return words.replace(word,'').replace('  ',' ').strip()

words=getRandStr(10,"абв")
print(words)
print(removeWords(words,"абв"))