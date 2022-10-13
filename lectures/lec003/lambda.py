def select (f,col):
    return [f(x) for x in col]
def where(f,col):
    return [x for x in col if f(x)]
def calc(op,a,b):
    return op(a,b)

print(calc(lambda a,b: a+b, 4,5))

data='1 2 3 5 8 15 23 38'.split()

res=select(int,data)
print(res)
res=where(lambda x: not x%2, res)
print(res)
res=select(lambda x: (x, x**2), res)
print(res)