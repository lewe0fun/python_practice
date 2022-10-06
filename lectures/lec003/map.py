# li=[x for x in range(1,20)]
# li=list(map(lambda x:x+10,li))
# print (li)

#data=list(map(int,input().split()))


# data=list(map(int,'1 2 3 4 5 6 7 8 9 10'.split()))
# print(data)


data=[x for x in range(10)]
res=list(filter(lambda i: i%2, data))
print(res)