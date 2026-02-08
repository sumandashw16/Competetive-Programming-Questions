# remember in sliding window problems you use i for shirking and j for expanding

x = [-3,6,1,8,5,-5,-3,8,8,1,4]
i = 0
j = 3

sum = sum(x[:4])
max_sum = sum
while(j<len(x)-1):
    sum = sum - x[i]
    i = i + 1
    j = j + 1
    sum = sum + x[j]
    max_sum = max(max_sum, sum)
print(max_sum)