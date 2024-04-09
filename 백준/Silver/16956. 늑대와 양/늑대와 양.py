import sys
input = sys.stdin.readline

r, c = map(int, input().split())
farm = []
for _ in range(r):
    farm.append(input().strip())

for i in range(r):
    for j in range(c):
        if farm[i][j] == "W": # 늑대일 경우
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: # 상하좌우
                if 0 <= x < r and 0 <= y < c: # 목장 범위 안이여야 함
                    if farm[x][y] == "S": # 양이면
                        print(0) # 0 출력 후 프로그램 종료
                        exit()
else:
    print(1)
    for i in range(r):
        print(farm[i].replace(".", "D"))