	#5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
#10
#-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
for i in range(len(numbers)):
    ii=random.randint(0, len(numbers)-1)
    temp=numbers[i]
    numbers[i]=numbers[ii]
    numbers[ii]=temp
print(numbers)