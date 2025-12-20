n,x,y = map(int, input().split())
first = min(x,y)
low = 0
high = max(x,y) * n
answer = 0
while low<high:
    mid = (low + high) // 2
    if mid//x + mid//y < n-1:
        low = mid + 1
    else:
        high = mid
        answer = high
print(answer + first)