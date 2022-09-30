# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def printDecToBin(dec):
    if dec==0:
        print(dec)
        return
    elif dec!=1:
        printDecToBin(dec//2)
    print(dec%2, end='')
    

printDecToBin(88)
print()
printDecToBin(11)