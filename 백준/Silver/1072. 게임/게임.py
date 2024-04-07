import sys
input = sys.stdin.readline

x, y = map(int, input().split()) # 게임 횟수, 이긴 게임
z = y * 100 // x # 승률 계산

if z >= 99:
    print(-1)
else:
    answer = -1
    start = 1
    end = x

    while start <= end:
        mid = (start + end) // 2
        percent = (y+mid) * 100 // (x+mid)

        if z >= percent:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    
    print(answer)