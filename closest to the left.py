import sys

input = sys.stdin.read
data = input().split()

iterator = iter(data)
n = int(next(iterator))
k = int(next(iterator))

xs = []
ys = []
for _ in range(n):
    xs.append(int(next(iterator)))
for _ in range(k):
    ys.append(int(next(iterator)))

def binary_search(target):
    low = 0
    high = n-1
    answer = -1
    while low <= high:
        mid = (low + high)//2
        if xs[mid] <= target:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    print(answer + 1)

for target in ys:
    binary_search(target)
