# remember in sliding window problems you use i for shirking and j for expanding

x = [1,2,6,3]
target = 5

i = 0
summation = 0
max_len = 0

for j in range(len(x)):
    summation += x[j]

    while summation > target:
        summation -= x[i]
        i += 1

    max_len = max(max_len, j - i + 1)

print(max_len)
