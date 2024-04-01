n = int(input())
wine = [0] * 10001
summ = [0] * 10001

for i in range(1, n+1):
    wine[i] = int(input())
    
summ[1] = wine[1]

if n>=2:
    summ[2] = max(wine[1], 0) + wine[2]

for i in range(3, n+1):
    summ[i] = max(summ[i-1], wine[i] + wine[i-1] + summ[i-3], wine[i] + summ[i-2])
    
print(summ[n])