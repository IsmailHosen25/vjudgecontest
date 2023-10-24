def min_max(arr):
    min=0
    max=0
    for i in range(0,len(arr)-1):
        min+=arr[i]
    for i in range(len(arr)-1,0,-1):
        max+=arr[i]
    print(min ,end=" ")
    print(max)

arr=list(map(int,input().split()))
min_max(arr)