n = int(input())
data = []
answer = 0

for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (-x[0], x[1]))
fifth = data[4][0]

for i in range(5, n):
    if data[i][0] == fifth:
        answer += 1

print(answer)