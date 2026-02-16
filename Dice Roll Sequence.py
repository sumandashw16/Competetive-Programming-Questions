t = int(input())
anamolies = {1: 6, 2: 5, 3: 4, 6: 1, 5:2, 4:3}
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(0,n,2):
        if(i == n-1):
            break
        elif(i == n-2):
            if(anamolies[a[i]] == a[i+1] or a[i] == a[i+1]):
                count += 1
        else:
            if(anamolies[a[i+1]] == a[i] or anamolies[a[i+1]] == a[i+2] or a[i+1] == a[i] or a[i+1] == a[i+2]):
                count += 1
    print(count)

        