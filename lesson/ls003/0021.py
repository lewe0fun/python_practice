from random import choices
def name(a, b):
    name= []
    for t in range(a):
        y=choices(b, k=3)
        name.append("".join(y))

    return name
my_list=name(10,"abc")
print(my_list)

def find (m, o: list):
    if m in o and o.count(m)>1:
        p=o.index(m)
        print(o.index(m, p+1))
    else: 
        print(-1)
find(input(), my_list)
