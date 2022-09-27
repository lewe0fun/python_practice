#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#in -> out
#- 6782 -> 23
#- 0.67 -> 13
#- 198.45 -> 27

digit=float(input('Введите число: '))
while True:
    digit*=10
    if digit%10==0:
        break
sum=0
while True:
    digit//=10
    sum+=(digit%10)
    if digit==0:
        break
print('Cумма цифр равна:',int(sum))
