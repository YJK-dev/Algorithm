import sys
input = sys.stdin.readline

def dfs(node, depth):
    global result
    visited[node] = True
    stack = [(node, depth)]  # DFS 스택에 현재 노드와 깊이를 튜플 형태로 저장

    while stack:
        node, depth = stack.pop()  # 스택에서 노드와 깊이를 꺼냄
        is_leaf = True  # 리프 노드인지 여부를 판단하기 위한 변수

        for next_node in graph[node]:
            if not visited[next_node]:
                is_leaf = False
                visited[next_node] = True
                stack.append((next_node, depth + 1))  # 다음 노드와 깊이를 스택에 추가

        if is_leaf:
            result += depth  # 현재 노드가 리프 노드일 경우 결과에 깊이를 더함

# 입력 처리
N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
result = 0

# 루트 노드인 1부터 DFS 시작
dfs(1, 0)

# 결과 출력
if result % 2 == 0:
    print("No")
else:
    print("Yes")
