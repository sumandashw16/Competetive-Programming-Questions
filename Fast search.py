n = int(input())
x = input()
xs = list(map(int, x.split()))
xs.sort()
def closest_to_the_left(target):
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
    return (answer + 1)

def closest_to_the_right(target):
    low = 0
    high = n - 1
    answer = n
    while(low<=high):
        mid = (low + high)//2
        if(target <= xs[mid]):
            answer = mid
            high = mid - 1
        elif(target>xs[mid]):
            low = mid + 1
    return (answer + 1)

k = int(input())
for i in range(k):
    l,h = map(int,input().split())
    right = closest_to_the_left(h)
    left = closest_to_the_right(l)
    print(max(0,right - left + 1), end =" ")