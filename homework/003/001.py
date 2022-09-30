#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
#in
#5

#out
#[10, 2, 3, 8, 9]
#22

# in
# 4

# out
# [4, 2, 4, 9]
# 8
from random import sample

def getRandomList(size):
    if size<0:
        size=-size
    result=sample(range(10),size)
    print(result)
    return result

def oddElemListSum(list):
    sum=0
    for i in range(len(list)):
        if i%2==0:
            sum+=list[i]
    return sum

print(oddElemListSum(getRandomList(int(input('Введите размер списка: ')))))
