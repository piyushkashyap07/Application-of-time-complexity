from sys import stdin


def intersection(arr1, arr2, n, m) :
    arr1.sort()
    arr2.sort()
    i=0
    j=0
    while i<n and j<m:
        if arr1[i]==arr2[j]:
            print(arr1[i],end=" ")
            i+=1
            j+=1
        else:
            if arr1[i]<arr2[j]:
                i+=1
            else:
                j+=1
                





























# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1