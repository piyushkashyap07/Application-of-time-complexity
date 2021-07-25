from sys import stdin

def tripletSum(arr, n, num) :
    arr.sort()
    count = 0
    for k in range(n - 2):
        i = k+1
        j = n-1
        while i<j:
            if arr[k] + arr[i] + arr[j] > num:
                j = j-1
            
            elif arr[k] + arr[i] + arr[j] < num:
                i = i + 1
                
            else:
                if arr[i] == arr[j]:
                	temp = j-i+1
                	count = count + ((temp)*(temp-1))//2
                	i=i+temp
                	j=j-temp
                    
                elif (arr[i] == arr[i+1]) or (arr[j] == arr[j-1]):
                    ti = 1
                    while arr[i] == arr[i+ti]:
                        ti += 1
                    
                    tj = 1
                    while arr[j] == arr[j-tj]:
                        tj += 1
                        
                    count = count + ti*tj
                    
                    i=i+ti
                    j=j-tj
                    
                else:
                    i=i+1
                    j=j-1
                    count = count + 1
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
    print(tripletSum(arr, n, num))

    t -= 1