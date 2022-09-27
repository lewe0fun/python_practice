# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
digit=int(input('введите число'))
for i in range(-digit, digit + 1):
    print(i, end=" ")