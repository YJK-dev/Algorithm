import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input()) # 참여 선수 수
    result = list(map(int, input().split())) # 팀 번호
    teams = {}
    counter = Counter(result) # 팀 당 주자 수 Counter({1: 6, 3: 6, 2: 2, 4: 1})
    cnt = 0
    for i in range(n):
        if counter[result[i]] < 6: # 팀원이 6명 이하이면
            cnt += 1
            continue
        if result[i] in teams:
            teams[result[i]].append(i-cnt)
        else:
            teams[result[i]] = [i-cnt]
    print(sorted(teams, key=lambda x: (sum(teams[x][0:4]), teams[x][4]))[0])