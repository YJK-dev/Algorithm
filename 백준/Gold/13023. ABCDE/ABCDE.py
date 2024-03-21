import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
arrive = False
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def DFS(now, depth):
  global arrive
  if depth == 5:
    arrive = True
    return
  visited[now] = True
  for next_node in graph[now]:
    if not visited[next_node]:
      DFS(next_node, depth+1) 
  visited[now] = False


for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(N):
  DFS(i, 1)
  if arrive:
    break

if arrive:
  print(1)
else:
  print(0)
  
