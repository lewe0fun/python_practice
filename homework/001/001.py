# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

while True:
    day=int(input('введите цифру, обозначающую день недели: '))
    if 0<day<8:
        break
if (day>5):
    print (day,'день недели - выходной')
else:
    print (day,'день недели - невыходной')