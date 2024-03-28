n = int(input())
data = []

for _ in range(n):
    name, korean, english, math = input().split()
    data.append((name, int(korean), int(english), int(math)))
    
data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(data[i][0])