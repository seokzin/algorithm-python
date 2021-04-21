from collections import deque

n = int(input())
k = int(input())

graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)

for _ in range(k):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(n):
  q = deque()
  q.append(n)

  while q:
    i = q.popleft()

    if visit[i] == 0:
      visit[i] = 1

      for j in graph[i]:
        q.append(j)

bfs(1)

print(sum(visit) - 1)

# 전체적으로 훑는게 BFS가 적합하다던데.. 내 코드는 BFS가 DFS보다 더 느렸다.
# 덱을 선언할 때 q로 하는게 좋지 않은 습관? 대부분 queue로 하는듯