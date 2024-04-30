from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))
q = deque(range(1, n+1))
cnt = 0

for num in nums:
  while q:
    if q[0] == num:
      q.popleft()
      break

    if q.index(num) <= len(q) // 2:
      q.rotate(-1)
      cnt += 1
    
    else:
      q.rotate(1)
      cnt += 1

    
print(cnt)