
path='test/data.txt'
data=open(path,'r')
arr=data.readline().split(' ')
data.close()
result=[]
for i in range(len(arr)):
    if int(arr[i])%2==0:
        temp=(int(arr[i]),int(arr[i])**2)
        result.append(temp)
print(result)