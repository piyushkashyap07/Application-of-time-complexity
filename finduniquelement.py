from sys import stdin

def findUnique(arr, n) :
    arr.sort()
    i=0
    while i<n-1:
        if arr[i]!=arr[i+1]:
            return arr[i]
        elif arr[i]==arr[i+1]:
            i+=2
    
    return arr[n-1]
        
    
            





























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
    print(findUnique(arr, n))

    t-= 1