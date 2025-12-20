n, k = map(int, input().split())
maxLength = 0
arr = []
high = 0
ans = 0
def calcSum(mid):
    sum = 0
    for i in range(n):
        sum = sum + arr[i]//mid
    return sum

for i in range(n):
    l = int(input())
    arr.append(l)
    high = high + l

right = high / k
left = 1e-6

for i in range(60):
    mid = (left + right)/2
    if (calcSum(mid) >= k):
        ans = mid
        left = mid
    else:
        right = mid

print(ans)