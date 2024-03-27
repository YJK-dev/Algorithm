n = int(input())
data = []
answer = 0

for _ in range(n):
    q_cnt, s_cnt = map(int, input().split())
    data.append((q_cnt, s_cnt))

data.sort(key=lambda x: (x[0], x[1]), reverse = True)

for i in range(5, n):
    if data[4][0] == data[i][0] and data[4][1] > data[i][1]:
        answer += 1

print(answer)