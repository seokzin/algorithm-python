import sys

input = sys.stdin.readline
INF = sys.maxsize # 2^63 - 1

def bf():
  for times in range(n):
    for v in range(1, n+1):
      for nv, nw in graph[v]:
        # dis[v] != INF - 시작점과 이어지지 않은 음의 사이클 건너뛰기 위해
        if dis[v] != INF and dis[nv] > dis[v] + nw:
          dis[nv] = dis[v] + nw
          if times == n-1:
            return True
  return False

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
dis = [INF] * (n+1)
dis[1] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

res = bf()

if res:
  print(-1)
else:
  for i in dis[2:]:
    print(i if i !=INF else -1)