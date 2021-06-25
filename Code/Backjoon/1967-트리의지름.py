from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1): # 노드 개수-1 = 간선
  a, b, w = list(map(int, input().split()))
  graph[a].append((b, w))
  graph[b].append((a, w))

max_dis = 0 # 최대거리
max_index = 0 # 최대거리의 노드

def bfs(start):
  global max_dis
  global max_index

  visit = [0] * (n+1)
  dis = [0] * (n+1)

  q = deque()
  q.append(start)
  visit[start] = 1

  while q:
    t = q.popleft()
    for i, d in graph[t]:
      if not visit[i]:
        visit[i] = 1
        dis[i] = dis[t] + d
        q.append(i)
        if max_dis < dis[i]:
          max_dis = dis[i]
          max_index = i

bfs(1)
bfs(max_index)

print(max_dis)

# 1167과 거의 똑같은 문제..