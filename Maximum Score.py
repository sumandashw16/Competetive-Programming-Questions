t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min = 0
    for i in range(n):
        if abs(A[i] - B[i]) < A[min] - B[min]:
            min = i
    print(sum(A) - A[min] + B[min])