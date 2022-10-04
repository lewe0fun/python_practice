# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
import random
def striptrepitDigitsList(digits):
    nonRepitDigits=[]
    for i in range(len(digits)):
        if digits.count(digits[i])==1:
            nonRepitDigits.append(digits[i])
    print(nonRepitDigits)
    return nonRepitDigits
def getRandomRepitValueList(length):
    if length<0:
        print('Отрицательное количество элементов!')
        return []
    digits = list(range(10))
    digits=random.choices(digits, k=length)
    print(digits)
    return digits

striptrepitDigitsList(getRandomRepitValueList(int(input('Размер списка:'))))