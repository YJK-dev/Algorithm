from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
order = [[] for _ in range(n)]

for i in range(n):
    order[i] = input().split()

for i in range(n):
    if order[i][0] == "push":
        q.append(order[i][1])

    elif order[i][0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif order[i][0] == "size":
        print(len(q))
    elif order[i][0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif order[i][0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif order[i][0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])
    