# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import choices
size=int(input('Размер списка чисел: '))
digits=choices(range(size*2), k=size)
print('Cписок чисел: ',digits)
print ('Cписок чисел, значения которых больше предыдущего элемента: ',[digits[i+1] for i in range(len(digits)-1) if digits[i]<digits[i+1]])


