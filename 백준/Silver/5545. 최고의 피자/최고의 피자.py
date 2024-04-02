import sys
input = sys.stdin.readline

n = int(input()) # 토핑 종류의 수 
dough_price, topping_price = map(int, input().split()) # 도우 가격, 토핑 가격
dough_cal = int(input()) # 도우의 열량
# 토핑 각각의 열량을 입력 받아 리스트에 저장하고 내림차순으로 정렬하기
t_cal_list = [int(input()) for _ in range(n)]
t_cal_list.sort(reverse=True)

# 초기 결과값은 도우 1원당 열량으로 설정
answer = dough_cal / dough_price

# 토핑은 1개에서 n개를 선택할 수 있다. 
# 반복문을 돌면서 누적으로 추가하여 최대 열량 비율을 찾는다.
for i in range(1, n+1):
    # 도우 기본 칼로리에 현재까지 선택한 토핑들의 열량의 총합을 더함
    current_cal = dough_cal + sum(t_cal_list[:i]) 
    # 도우 기본 가격에 현재까지 선택한 토핑 가격 총합을 더한다.
    current_price = dough_price + (topping_price * i)
    
    # 현재 피자의 1원당 열량 계산
    current_calorie_ratio = current_cal / current_price

    # 현재 열량 비율이 기존의 최대 열량 비율보다 높다면 업데이트함
    if current_calorie_ratio > answer:
        answer = current_calorie_ratio

#1원당 열량이 가장 높은 피자의 1원당 열량을 출력(정수로 변환하여 소수점 이하 제거)
print(int(answer)) 

