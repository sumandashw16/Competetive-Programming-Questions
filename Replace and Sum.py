t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    lr = [tuple(map(int, input().split())) for _ in range(q)]

    for i in range(n):
        if a[i] < b[i]:
            a[i] = b[i]

    mx = a[-1]
    for i in range(n-2, -1, -1):
        if a[i] < mx:
            a[i] = mx
        else:
            mx = a[i]

    pref = [0]*(n+1)
    for i in range(n):
        pref[i+1] = pref[i] + a[i]

    ans = []
    for l, r in lr:
        ans.append(str(pref[r] - pref[l-1]))

    print(" ".join(ans))
