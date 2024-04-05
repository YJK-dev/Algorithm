import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = []
for i in range(n):
    age, name = input().split()
    a.append((int(age), name))

a.sort(key=lambda x: (x[0]))

for member in a:
    print(member[0], member[1])