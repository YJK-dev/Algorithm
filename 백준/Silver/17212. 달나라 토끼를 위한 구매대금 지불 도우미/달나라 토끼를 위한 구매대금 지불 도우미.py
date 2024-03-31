n = int(input())
dy = [0] * 100001
dy[1] = 1
dy[2] = 1
dy[3] = 2
dy[4] = 2
dy[5] = 1
dy[6] = 2
dy[7] = 1

if n <= 7:
    print(dy[n])
else:
    for i in range(8, n+1):
        dy[i] = 1 + min(dy[i-1], dy[i-2], dy[i-5], dy[i-7])

    print(dy[n])
