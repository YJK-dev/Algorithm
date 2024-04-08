import sys
input = sys.stdin.readline

n = int(input()) # 옷의 종류의 수
d = list(map(int, input().split())) # 각 종류별 옷의 개수를 저장한 리스트
total_clothes = sum(d) # 전체 옷 개수

# 사람이 1명만 있다면 인접한 경우 존재 안함
if n == 1 and d[0] == 1:
    print("Happy")
# 가장 많은 옷을 가진 종류의 개수가 전체 옷 개수의 절반을 넘지 않으면 안겹침
else:
    if total_clothes //2 >= max(d):
        print("Happy")
    else:
        print("Unhappy")