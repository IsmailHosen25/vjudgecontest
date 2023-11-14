n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range (n):
        if a[i] == b[j] and a[i] > 0:
            res += 1
            a[i] = 0 #just set to 0 to be not used anymore
            b[j] = 0

if res < n:
    res += 1
else:
    res -= 1

print (res)