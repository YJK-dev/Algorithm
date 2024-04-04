N = int(input())
P = list(map(int, input().split()))
P.sort()
usetime_list = [0]*N # N명 각각의 소요시간 list
usetime_list[0] = P[0]

for i in range(1, N):
    usetime_list[i] = usetime_list[i-1] + P[i]

print(sum(usetime_list))
