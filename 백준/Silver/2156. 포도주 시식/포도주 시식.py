import sys
input = sys.stdin.readline

n = int(input().strip())
wine = [0] * 10001
dy = [0] * 10001

for i in range(1, n+1):
    wine[i] = int(input())
    
dy[1] = wine[1]
dy[2] = wine[1] + wine[2]

for i in range(3, n+1):
    dy[i] = max(dy[i-1], wine[i]+wine[i-1]+dy[i-3], wine[i]+dy[i-2])
    
print(dy[n])