from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
res = [[0] * (n+1) for _ in range(n+1)]
degree = [0] * (n+1) # 진입차수 관리
q = deque()

for _ in range(m):
  x, y, k = map(int, input().split())
  graph[y].append((x, k)) # 이렇게 넣는게 핵심인듯..
  degree[x] += 1

for i in range(1, n+1):
  if degree[i] == 0:
    q.append(i)

while q:
  v = q.popleft()
  
  for n_v, n_w in graph[v]:
    if sum(res[v]) == 0: # 기본 부품이면
      res[n_v][v] += n_w

    else: # 중간 부품이면 -> 기존 부품들에 가중치를 곱
      for i in range(1, n+1):
        res[n_v][i] += res[v][i] * n_w
        
    degree[n_v] -= 1

    if degree[n_v] == 0:
      q.append(n_v)

for res in enumerate(res[n]):
  if res[1] > 0:
    print(*res)

# 위상 정렬 -> 사이클 없고 시작과 종료가 명확할 때 (스택보단 큐 선호)
# print(*res if res[1] > 0 else continue) -> 에러. continue는 statement기 때문에 expression 안에 있을 수 없다.

