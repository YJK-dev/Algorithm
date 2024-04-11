n, k, a, b = map(int, input().split())
pot = [k]*n
day = 0

while 0 not in pot:
    for i in range(a):
        pot[i] += b
    
    for i in range(len(pot)):
        pot[i] -= 1
    
    pot.sort()
    day += 1

print(day)