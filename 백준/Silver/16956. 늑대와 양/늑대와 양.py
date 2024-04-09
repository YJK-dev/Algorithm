import sys
input = sys.stdin.readline

def main():
    r, c = map(int, input().split())
    farm = [input().strip() for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if farm[i][j] == "W": # 늑대일 경우
                if check_surroundings(farm, r, c, i, j):
                    print(0) # 0 출력 후 프로그램 종료
                    return

    print(1)
    for row in farm:
        print(row.replace(".", "D"))

def check_surroundings(farm, r, c, i, j):
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: # 상하좌우
        if 0 <= x < r and 0 <= y < c and farm[x][y] == "S":
            return True
    return False

if __name__ == "__main__":
    main()
