# 5. ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!
def lineCountInFile(path):
    file=open(path,'r')
    lines = 0
    for line in file:
        if line != "\n":
            lines+=1
    return lines
def mergeLinesInFles(path1,path2):
    if lineCountInFile(path1)!=lineCountInFile(path2):
        print('The contents of the files do not match!')
        return
    poly1=open(path1,'r')
    poly2=open(path2,'r')
    with open('homework/004/polySum.txt','w') as result:
        for i in range(lineCountInFile(path1)):
            result.write(poly1.readline().replace('=0\n','+')+poly2.readline())

    poly1.close()
    poly2.close()


path1='homework/004/poly1.txt'
path2='homework/004/poly2.txt'

mergeLinesInFles(path1,path2)