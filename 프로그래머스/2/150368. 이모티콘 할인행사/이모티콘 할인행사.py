from itertools import product

def solution(users, emoticons):
    answer = [] # 결과를 저장할 리스트
    
    discountRate = [10, 20, 30, 40] # 이모티콘 할인율 리스트
    
		# 모든 할인율 조합에 대해 반복(중복순열 사용)
    for case in product(discountRate, repeat=len(emoticons)):
        subscriber = 0 # 이모티콘 플러스 서비스 가입자 수
        revenue = 0 # 이모티콘 판매 매출액

				# 각 사용자에 대해 반복
        for user in users:
            temp = 0 # user의 이모티콘 구입 비용
            # 각 이모티콘에 대해 할인율을 적용하여 비용 계산
            for idx, sale in enumerate(case):
                if sale >= user[0]: # 이모티콘 할인율이 유저가 원하는 할인율 이상이면 구매
                    temp += emoticons[idx] * (100 - sale) // 100 # 할인율 적용해 비용 계산

            if temp >= user[1]: # 유저 예산보다 비용이 초과하면 이모티콘플러스 가입
                subscriber += 1
            else:  # 플러스에 가입안하면 revenue에 이모티콘 구매 비용 누적
                revenue += temp

        # 해당 할인율 경우에서 구한 가입자 수와 매출을 answer에 추가
        answer.append([subscriber, revenue]) 
        
		# 결과 리스트를 가입자 수와 매출을 기준으로 내림차순 정렬
    answer.sort(key=lambda x: (-x[0], -x[1]))

    return answer[0] # 행사 목적을 최대한으로 달성한 결과를 반환