import math

def solution(fees, records):
    basic_time, basic_charge = fees[0], fees[1] # 기본 시간, 기본 요금
    unit_time, unit_charge = fees[2], fees[3] # 단위 시간, 단위 요금

    cars = {} # 주차장에 차 저장
    total_time = {} # 주차 시간 저장
    charges = {} # 주차 요금 저장
    

    def time_to_minute(time): # 시간을 분 단위로 바꾸는 함수
        h, m = time.split(':')
        minute = int(h) * 60 + int(m)
        return minute
    
    # 주차요금 계산 함수
    def parking_fee_calculator(parking_time): 
        if parking_time <= basic_time:
            return basic_charge
        else:
            extra_time = parking_time - basic_time
            extra_charge = math.ceil(extra_time/unit_time)*unit_charge
            return basic_charge + extra_charge
        
        
    # 입출차기록 확인
    for x in records:
        a, b, c = x.split() # 시각 차량번호 내역

        if c == 'IN': # 입차하면 입차시간을 저장
            cars[b] = time_to_minute(a)

        elif c == "OUT": # 출차하면 이용시간(출차시간-입차시간) 계산
            out_time = time_to_minute(a)
            parking_time = out_time - cars[b]  
            if b in total_time:
                total_time[b] += parking_time
            else:
                total_time[b] = parking_time   
            del cars[b] # 출차했으니 삭제


    # 주차 요금 계산
    # car에 차량번호가 남아있으면 23:59에 출차된 것으로 간주해 계산
    # 누적 주차 시간이 기본 시간 전후인지 확인해서 계산
    for car, entry_time in cars.items():
        try:
            total_time[car] += time_to_minute("23:59") - entry_time
        except:
            total_time[car] = time_to_minute("23:59") - entry_time
    
    answer = [parking_fee_calculator(time) for number, time in sorted(list(total_time.items()), key=lambda x: x[0])]
		
    return answer
