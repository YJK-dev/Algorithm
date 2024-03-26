def solution(participant, completion):
    answer = ''
    
    # 동명이인을 세기 위해 이름 등장 횟수를 저장하는 딕셔너리
    participant_dict = dict()
    
    # 참가자 명단 확인
    for name in participant:
        if name in participant_dict: # 동명이인 경우
            participant_dict[name] += 1
        else:
            participant_dict[name] = 1
    
   # 완주자 이름을 딕셔너리에서 제거
    for name in completion:
        participant_dict[name] -= 1
    
    # 완주 못한 참가자명 찾기
    for name, count in participant_dict.items():
        if count > 0:
            answer = name
            break
    
    return answer