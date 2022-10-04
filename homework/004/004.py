# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
import random
def formulaLogs(k):
    operator=['-','+']
    with open('homework/004/Log.txt','a',encoding='utf-8') as Log:
        for i in range(k):
            coef=random.randint(0,10)
            oprIndx=random.randint(0,1)
            pow=k-i
            skip=False
            if coef!=0:
                Log.write(str(coef))
                if pow>1:
                    Log.write('*x^'+str(pow))
                if pow==1:
                     Log.write('*x')
            if coef==1:
                if pow>1:
                    Log.write('x^'+str(pow))
                if pow==1:
                     Log.write('x')
            if coef==0:
                skip=True
            if not skip:
                Log.write(str(operator[oprIndx]))
        Log.write(str(random.randint(0,10))+'=0\n')

for i in range(2,9):             
    formulaLogs(i)
