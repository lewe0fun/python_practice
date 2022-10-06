
path='lectures/lec003/data.txt'
data=open(path,'r')

arr=data.readline().split(' ')
data.close()
result=[]
for i in range(len(arr)):
    if int(arr[i])%2==0:
        temp=(int(arr[i]),int(arr[i])**2)
        result.append(temp)
print(result,'Через итерациию:')

# через map и list complehentions
data=open(path,'r')
arr2=list(map(int,(data.readline().split(' '))))
data.close()
result2=[(arr2[i], arr2[i]**2) for i in range(len(arr2)) if arr2[i]%2==0]
print(result2,'Через map и list complehentions')