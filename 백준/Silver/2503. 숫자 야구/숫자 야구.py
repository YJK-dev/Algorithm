from itertools import permutations

def check_strike_ball(question, candidate):
    strike = ball = 0
    for i in range(3):
        if candidate[i] == question[i]:
            strike += 1
        elif candidate[i] in question:
            ball += 1
    return strike, ball

n = int(input())
candidates = [''.join(p) for p in permutations('123456789', 3)]

questions = []
results = []

for _ in range(n):
    question, strike, ball = map(int, input().split())
    questions.append((str(question), strike, ball))  

for candidate in candidates:
    temp = True
    for question, strike, ball in questions:
        s_cnt, b_cnt = check_strike_ball(question, candidate)

        if s_cnt != strike or b_cnt != ball:
            temp = False
            break

    if temp == True:
        results.append(candidate)

print(len(results))  
