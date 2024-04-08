import sys
input = sys.stdin.readline

m, n = map(int, input().split())
sticks = list(map(int, input().split()))

start = 1
end = max(sticks)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for stick in sticks:
        cnt += stick // mid

    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)