m = int(input())

def digit_sum(t: int):
    summation = 0
    for i in str(t):
        summation = summation + int(i)
    return summation

for i in range(m):
    x = int(input())
    if(x % 9 == 0):
        count = 0
        for i in range(x, x + 101):
            if (x + digit_sum(i) == i):
                count += 1
            else:
                pass
        print(count)
    else:
        print(0)
