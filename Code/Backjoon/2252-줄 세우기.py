from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
degree = [0] * (n+1) # 진입차수 관리
res = []

q = deque()

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  degree[b] += 1

for i in range(1, n+1):
  if degree[i] == 0:
    q.append(i)

while q:
  x = q.popleft()
  
  for y in graph[x]:
    degree[y] -= 1

    if degree[y] == 0:
      q.append(y)

  res.append(x)

print(*res)