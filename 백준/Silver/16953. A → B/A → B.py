A, B = map(int, input().split())

count = 0

while B > A:
    if B % 2 == 0:
        B //= 2
        count += 1
    elif B % 10 == 1:
        B //= 10
        count += 1
    else:
        print(-1)
        break
else:  # while 반복문이 break 없이 정상 종료됐을 때
    if B != A:  # B와 A가 같지 않으면 -1 출력
        print(-1)
    else:
        print(count+1)