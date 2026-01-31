x = [2,5,8,19,3]
target = 7
m = False
times = 0
for i, j in enumerate(x):
    for k in range(i+1,len(x)):
        times = times + 1
        if(j + x[k]==target):
            m = True
            break
    if(m):
        break

if(m):
    print("Yes")
else:
    print("No")

print(times)