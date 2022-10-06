import random
def getArr():
    path='lesson/ls005/n.txt'
    data= open(path,'r')
    arr=list(map(int,(data.readline().split(' '))))
    data.close()
    
    arr.remove(random.choice(arr))
    print(arr)
    return arr

def checkArr2(arr):
    if arr[0]!=0:
        return 0
    for i in range(1,len(arr)):
        if (arr[i]-1)!=arr[i-1]:
            return (arr[i])-1
    return -1

print(checkArr2(getArr()))