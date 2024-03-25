import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
enter = set()

for _ in range(n):
    user = input().strip()
    if user == "ENTER":
        cnt += len(enter)
        enter.clear()
    else:
        enter.add(user)

cnt += len(enter)
print(cnt)