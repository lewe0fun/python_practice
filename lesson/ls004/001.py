# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.

def isStringOfDigits(string):
    list=string.split()
    for i in list:
        if not i.strip("-").isdigit():
            return []
        return list
def minMax(list):
    if list:
        return min(list, key=int),max(list, key=int)
    return []

print(minMax(isStringOfDigits("23 23 56 -36")))