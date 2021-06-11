import heapq

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)] # 간선 정보 담은 리스트
dp = [] * (v + 1) # 가중치
heap = []

for i in range(e):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))
    
def dijkstra(start):
  graph[start] = 0
  heapq.heappush(heap, (0, start))
  while heap:
    w, n = heapq.heappop(heap)
    for n_n, wei in graph[n]:
      n_w = wei + w
      if n_w < dp[n_n]:
        dp[n_n] = n_w
        heapq.heappush(heap, [n_w, n_n])



dijkstra(k)

for i in dp[1:]:
  print(i if not i else "INF")

# 다익스트라 알고리즘 - 하나의 정점에서 나머지 모든 정점까지의 최단거리
# 푸시 인자로 tuple과 list의 차이..