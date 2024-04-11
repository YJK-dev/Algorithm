import math

def solution(n, stations, w):
    answer = 0 # 설치할 기지국의 최소 개수
    distance = [] # 전파가 닿지 않는 거리 범위를 저장할 리스트

    #1번 아파트부터 맨 앞 기지국 사이에 전파가 닿지 않는 거리 저장
    front = stations[0]-w-1
    distance.append(front)
    
    # 맨 마지막 기지국부터 마지막 아파트 사이에 전파가 닿지 않는 거리 저장
    back = n-stations[-1]-w
    distance.append(back)
    
    # 기지국 사이에 전파가 닿지 않는 거리 저장
    for i in range(1, len(stations)):
        middle = (stations[i]-w-1) - (stations[i-1]+w)
        distance.append(middle)
    
    for dis in distance:
        # 닿지 않는 거리가 0 이하일 경우 넘어간다.
        if dis <= 0:
            continue
        # 닿지 않는 거리에 설치할 기지국의 최소 개수를 누적한다.
        answer += math.ceil(dis / ((w*2)+1))

    return answer