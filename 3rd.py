def diagonalDifference(arr):
    temp = 0
    emp = 0
    for i in range(0,len(arr)):
        temp = temp + arr[i][i]
    
    for j in range(0,len(arr)):
        emp = emp + arr[j][len(arr)-1-j]
    
    return abs(temp - emp)

n = int(input())

arr = []

for _ in range(n):
        arr.append(list(map(int, input().split())))

result = diagonalDifference(arr)
print(result)