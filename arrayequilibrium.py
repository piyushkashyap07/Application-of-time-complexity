from sys import stdin

'''def arrayEquilibriumIndex(arr, n) :
    i=1
    while i<n:
        suml=sum(arr[0:i])
        sumr=sum(arr[i+1:])
        if suml==sumr:
            return i
        else:
            i+=1
    return -1

#Taking input using fast I/O method
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
    print(arrayEquilibriumIndex(arr, n))

    t-= 1'''
def equilibriumIndex(arr):
    if len(arr)==0:
        return -1
    else:
        n=len(arr)
        s=0
        for i in range(n):
            s=s+arr[i]
        l=arr[0]
        c=1
        c=1
        for i in range(1,n):
            r=s-l
            l=l+arr[i]
            if l==r:
                return i
                break
            else:
                c=c+1
        if c==n:
            return -1
    # Please add your code here
# Main
t=int(input())
while t>0:
    
    n = int(input())
    arr = [int(i) for i in input().strip().split()]
    print(equilibriumIndex(arr))
    t-=1