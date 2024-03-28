# 시리얼 번호의 모든 자리수의 합을 구하는 함수
def get_sum(s):
    res = 0
    for i in s: 
        if i.isdigit():
            res += int(i)
    return res

n = int(input()) # 기타의 개수 입력받기
data = [] # 시리얼번호 저장할 리스트

# 시리얼번호 입력받아 저장하기
for _ in range(n):
    data.append(input().rstrip())

# 첫번째 정렬 조건) 시리얼번호 길이 짧은 순서
# 두번째 정렬 조건) 시리얼번호 자릿수의 합이 작은 순서
# 세번째 정렬 조건) 사전 순서(=오름차순)
data.sort(key=lambda x: (len(x), get_sum(x), x))

# 시리얼 번호를 정렬한 결과를 출력
for x in data:
    print(x)