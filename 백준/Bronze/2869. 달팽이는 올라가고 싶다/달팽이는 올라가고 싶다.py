import sys, math
input = sys.stdin.readline

noon, night, length = map(int, input().split())

distance_to_climb = length - noon
climb_per_day = noon - night
cnt = 0

if distance_to_climb % climb_per_day == 0:
    cnt = 1 + distance_to_climb // climb_per_day
else:
    cnt = 1 + math.ceil(distance_to_climb / climb_per_day)

print(cnt)

