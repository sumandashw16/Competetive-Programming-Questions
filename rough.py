z = int(input())
for _ in range(z):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    pos = {v:i for i,v in enumerate(p)}
    possible = True
    for i in range(1,n):
        if a[i] != a[i-1] and pos[a[i]] < pos[a[i-1]]:
            possible = False
            break

    print("YES" if possible else "NO")
