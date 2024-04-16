from collections import deque
import sys

input = sys.stdin.readline

l, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(l)]
visited = [[False] * w for _ in range(l)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= w:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1

    return cnt

paint = []
for i in range(l):
    for j in range(w):
        if graph[i][j] == 1 and not visited[i][j]:
            paint.append(bfs(graph, i, j))

print(len(paint))
print(max(paint) if paint else 0)
