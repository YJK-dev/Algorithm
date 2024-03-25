n = int(input())

in_dic = {}
out_list = []

cnt = 0

for i in range(n):
    car_number = input()
    in_dic[car_number] = i

for _ in range(n):
    out_list.append(input())

for i in range(n-1):
    for j in range(i+1, n):
        if in_dic[out_list[i]] > in_dic[out_list[j]]:
            cnt += 1
            break

print(cnt)

