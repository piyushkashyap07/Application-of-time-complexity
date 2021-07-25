from sys import stdin

def pairSum(arr,x) :
    arr.sort()
    i=0
    j=n-1
    count=0
    while i<j:
        if arr[i]+arr[j]>num:
            j-=1
        elif arr[i]+arr[j]<num:
            i+=1
        else:
            if arr[i]==arr[j]:
                l=j-i+1
                loop=(l*(l-1))//2
                for k in range(loop):
                    count+=1
                i=j
            else:
                counti=arr.count(arr[i])
                countj=arr.count(arr[j])
                count+=(counti*countj)
                i+=counti
                j-=countj
    return count







#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    ans=pairSum(arr,num) 
    print(ans)

    t -= 1