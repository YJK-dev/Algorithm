from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]

visited = [[0] * n for _ in range(m)]
white, black = 0, 0
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1 # 근처 아군 세는 변수

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    
    return cnt

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            answer = bfs(i, j)
            if graph[i][j] == "W":
                white += answer ** 2
            else:
                black += answer ** 2

print(white, black)