#* 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
#Position one: 1
#Position two: 3
#Number of elements: 5
#-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#-> 15
while True:
    limits=int(input('Число элементов: '))
    if limits>0:
        break
length=2*limits+1
while True:
    print('Введите значения от 1 по ', length)
    pos1=int(input('Позиция 1: '))
    pos2=int(input('Позиция 2: '))
    if (0<pos1<length+1) and (0<pos2<length+1):
        break
numbers=[0]*length
for i in range(length):
    numbers[i]=-limits+i
print(numbers)
print('Произведение элемтов массива', pos1,' и ', pos2,' равно', numbers[pos1-1]*numbers[pos2-1])