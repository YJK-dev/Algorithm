import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    k = int(input().rstrip())
    n = int(input().rstrip())

    a =[[0]*(n+1) for _ in range(k+1)]

    for i in range(n+1):
        a[0][i] = i

    for i in range(1, k+1):
        for j in range(1, n+1):
            a[i][j] = a[i][j-1] + a[i-1][j]

    print(a[k][n])