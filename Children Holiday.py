m, n = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

numberBalloon = []

def calcNumber(mid):
    numberBalloon.clear()
    for i in arr:
        value = i[0] * i[1] + i[2]
        rem = mid % value
        quote = mid // value
        balloons = quote * i[1]
        if rem >= i[0]:
            balloons += min(i[1], rem // i[0])
        numberBalloon.append(balloons)

high = 10**7
low = 0

while (low < high):
    mid = (high + low) // 2
    calcNumber(mid)
    if sum(numberBalloon) >= m:
        high = mid
    else:
        low = mid + 1

print(high)
calcNumber(high)
remaining = m
for i in numberBalloon:
    display = min(remaining, i)
    print(display, end=" ")
    remaining -= display
