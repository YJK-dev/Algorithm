import sys
input = sys.stdin.readline

def backtracking(muscle, days):
    global cnt
    if muscle < 500:
        return
    if days == n:
        cnt += 1
        return
    muscle -= k # 근손실
    for i in range(n):
        if not visited[i]: # 키트 사용 안했을 경우
            visited[i] = 1
            backtracking(muscle+a[i], days+1)
            visited[i] = 0


n, k = map(int, input().split()) # 날짜수, 하루중량감소량
a = list(map(int, input().split())) # 각 운동 키트의 중량 증가량
muscle = 500
cnt = 0
visited = [0] * n

backtracking(muscle, 0)
print(cnt)
