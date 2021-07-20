from collections import deque

def bfs(start, end):
  q = deque()
  q.append(start)
  visit = [0 for _ in range(n+1)]
  dis = [0 for _ in range(n+1)]

  visit[start] = 1

  while q:
    v = q.popleft()

    for i_n, i_w in graph[v]:
      if visit[i_n] == 0:
        q.append(i_n)
        visit[i_n] = 1
        dis[i_n] += dis[v] + i_w

        if i_n == end:
          return dis[i_n]


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  u, v, w = map(int, input().split())
  graph[u].append([v, w])
  graph[v].append([u, w])

for _ in range(m):
  start, end = map(int, input().split())
  print(bfs(start, end))



# []*(n+1) 은 안된다. copy 관련해 확실히 찾기
# 그래프 자체가 Spanning Tree다. 다익스트라까진 필요 없다.
# 더 이쁘게 만들 수 있을 것 같다. 나중에