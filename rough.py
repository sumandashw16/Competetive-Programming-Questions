t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    i = 0
    while i < n - 1:
        if a[i] == a[i+1] or a[i] + a[i+1] == 7:
            count += 1
            i += 2
        else:
            i += 1
    print(count)