w, h, n = map(int, input().split())

left = 0
right = max(w,h)*n

while(left<right):
    mid = (left + right) // 2
    if(mid//w * mid//h > n):
        right = mid
    else:
        left = mid + 1
print(left)

