def solve(a, n):
    leftSum = 0
    rightSum = 0
    for i in range(1, n):
        rightSum += a[i]
    for i in range(n-1):
        j = i + 1
        if leftSum == rightSum:
            return True
        leftSum += a[i]
        rightSum -= a[j]
    return False

T = int(input())
while T > 0:
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1 or solve(a, n):
        print("YES")
    else:
        print("NO")
    T -= 1

