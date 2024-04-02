import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 자연수 범위, 순열 길이 입력받기
answer = [] # 결과를 저장할 리스트
visited = [False]*(n+1) # 방문 여부를 저장할 리스트, False로 초기화

def dfs(depth):
    # 함수종료조건) depth가 m이 되면 
    # 즉, 선택한 숫자의 개수가 m과 같다면, 현재까지 선택한 숫자들을 출력
    if depth == m:
        print(*answer)
        return
    
    # 1부터 n까지의 숫자를 탐색
    for i in range(1, n+1):
        # 이미 방문한 숫자라면 건너뜀
        if visited[i] == True:
            continue
        # 방문하지 않은 숫자라면
        else:
            # 해당 숫자를 방문했다고 표시하고 결과 리스트에 추가
            visited[i] = True
            answer.append(i)

            # 다음 depth에서 탐색을 계속 진행하기 위해 재귀 호출
            dfs(depth+1)

            # 백트래킹: 다시 방문하지 않은 상태로 변경하고 결과 리스트에서 숫자 제거
            visited[i]=False
            answer.pop()

#dfs를 수행하여 0부터 시작해서 길이가 M이 될 때까지 모든 경우의 수를 탐색
dfs(0)