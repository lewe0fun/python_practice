# 4. Напишите программу, которая будет принимать на вход дробь
#    и показывать первую цифру дробной части числа.
digit=float(input('введите число\n'))
print(int(digit*10%10))