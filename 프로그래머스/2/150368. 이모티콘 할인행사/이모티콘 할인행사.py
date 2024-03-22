from itertools import product

def solution(users, emoticons):
    answer = []
    
    discountRate = [10, 20, 30, 40]

    for case in product(discountRate, repeat=len(emoticons)):
        # 각 테스트 케이스마다 subscriber와 revenue 초기화
        subscriber = 0
        revenue = 0

        for user in users:
            temp = 0 # user의 이모티콘 구입 지불 비용
            for idx, sale in enumerate(case):
                if sale >= user[0]: # 이모티콘 할인율이 유저가 원하는 할인율 이상이면 구매
                    temp += emoticons[idx] * (100 - sale) // 100

            if temp >= user[1]: # 유저 예산보다 비용이 초과하면 이모티콘플러스 가입
                subscriber += 1
            else:
                revenue += temp

        answer.append([subscriber, revenue])

    answer.sort(key=lambda x: (-x[0], -x[1])) # 이모티콘플러스 가입자 최대, 이모티콘 판매액 최대로 정렬

    return answer[0] # 가장 큰 값을 반환
