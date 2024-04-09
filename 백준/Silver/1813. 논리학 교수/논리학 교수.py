n = int(input())
case = list(map(int, input().split()))

answer = -1

for i in range(n+1):
    true_count = case.count(i)

    if true_count == i:
        answer = max(answer, i)

print(answer)

