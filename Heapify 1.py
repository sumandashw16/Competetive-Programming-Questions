t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    can_sort = True
    for i in range(1, n + 1):
        pos = i
        while pos % 2 == 0:
            pos //= 2
            
        val = a[i]
        while val % 2 == 0:
            val //= 2
            
        if pos != val:
            can_sort = False
            break    
    if can_sort:
        print("YES")
    else:
        print("NO")